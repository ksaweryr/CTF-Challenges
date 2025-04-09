def next_seed(s):
    return (75 * s + 74) % 65537


def from_seed(s):
    return (s & 0xf) | ((s >> 4) & 0xf0)


with open('libinterop.so', 'rb') as f:
    data = f.read()

data2 = []
s = 4629

for b in data:
    s = next_seed(s)
    data2.append(b ^ from_seed(s))

with open('libinterop.so.enc', 'wb') as f:
    f.write(bytes(data2))
