from Crypto.Cipher import ARC4
from datetime import datetime

from solve import *


def encrypt():
    with open('moon.bmp', 'rb') as f:
        data = f.read()
    header = data[:0x8a]
    plaintext = data[0x8a:]
    dt = datetime.strptime('31 Jan 2020, 20:38:42 +0000', '%d %b %Y, %H:%M:%S %z')
    seed = int(dt.timestamp())
    e = LuaXoshiro(seed)
    key = str(lua_nth_random(e, 1_000_000_000_000_000)).encode()
    cipher = ARC4.new(key, drop=3072)
    ciphertext = cipher.encrypt(plaintext)
    with open('chall.bmp', 'wb') as f:
        f.write(header + ciphertext + b'31 Jan 2020, 20:38')


if __name__ == '__main__':
    encrypt()
