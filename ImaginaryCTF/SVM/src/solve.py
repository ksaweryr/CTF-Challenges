import struct
from z3 import *

with open('output.bin', 'rb') as f:
    data = f.read()

numbers = struct.unpack('<' + 'i' * 40, data)

flag = ''

for i in range(10):
    results = numbers[4*i:4*(i + 1)]
    s = Solver()
    chars = [Int(f'char_{j}') for j in range(4)]
    s.add(2 * chars[3] - 5 * chars[2] + 12 * chars[1] + 7 * chars[0] == results[0])
    s.add(1 * chars[3] + 10 * chars[2] + 4 * chars[1] + 42 * chars[0] == results[1])
    s.add(3 * chars[3] + 17 * chars[2] - 8 * chars[1] - 3 * chars[0] == results[2])
    s.add(7 * chars[3] + 21 * chars[2] + 1 * chars[1] + 15 * chars[0] == results[3])
    assert s.check() == sat
    m = s.model()
    for c in chars:
        flag += chr(m[c].as_long())

print(flag)
