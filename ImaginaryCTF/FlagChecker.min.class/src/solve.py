from z3 import *

expr = 'array[0] == 105 && array[1] == 99 && array[2] == 116 && array[3] == 102 && array[4] == 123 && array[17] == 125 && -21 * array[5] + 1 * array[6] + 1 * array[7] + 1 * array[8] + 1 * array[9] + 1 * array[11] + -2 * array[12] + -8 * array[13] + -3 * array[14] + -1 * array[15] + -1 * array[16] == -3048 && 2 * array[5] + -1 * array[6] + -1 * array[9] + 4 * array[10] + 2 * array[11] + 5 * array[12] + 1 * array[13] + 1 * array[14] + 1 * array[15] + -2 * array[16] == 1283 && 1 * array[5] + 7 * array[6] + 2 * array[7] + -1 * array[8] + -1 * array[9] + 1 * array[11] + -1 * array[14] + -3 * array[15] == 592 && 2 * array[5] + -1 * array[6] + -1 * array[8] + 1 * array[9] + -151 * array[10] + -1 * array[11] + 1 * array[12] + -3 * array[14] + 2 * array[15] + 20 * array[16] == -15721 && -1 * array[5] + -1 * array[6] + -21 * array[7] + 2 * array[8] + -4 * array[10] + -2 * array[11] + -3 * array[13] + -6 * array[14] + 3 * array[16] == -3620 && -1 * array[6] + 1 * array[7] + -1 * array[8] + -98 * array[9] + -1 * array[10] + -1 * array[11] + -4 * array[12] + 1 * array[13] + 1 * array[15] + -4 * array[16] == -10482 && 3 * array[5] + 4 * array[7] + -14 * array[8] + 1 * array[9] + 27 * array[10] + 2 * array[11] + 1 * array[12] + -7 * array[13] + 1 * array[14] + -1 * array[15] + -3 * array[16] == 1927 && -1 * array[5] + -1 * array[7] + -4 * array[8] + -95 * array[9] + 1 * array[10] + -47 * array[11] + -1 * array[12] + 8 * array[13] + 3 * array[14] + -1 * array[15] + -1 * array[16] == -14402 && 1 * array[5] + 1 * array[6] + -4 * array[7] + 3 * array[8] + -1 * array[9] + -3 * array[10] + -1 * array[11] + 8 * array[14] + -1 * array[16] == 175 && -1 * array[5] + 4 * array[8] + -1 * array[10] + -1 * array[12] + 2 * array[13] + -3 * array[14] + 1 * array[15] + -22 * array[16] == -2024 && -1 * array[5] + -7 * array[6] + 1 * array[7] + -2 * array[8] + 9 * array[9] + 1 * array[10] + 20 * array[11] + 1 * array[12] + -4 * array[13] + -1 * array[14] + -1 * array[15] + -6 * array[16] == 1210 && 2 * array[5] + 3 * array[6] + 1 * array[7] + 1 * array[8] + 2 * array[9] + -1 * array[10] + -1 * array[11] + 5 * array[12] + 1 * array[13] + 11 * array[14] + -5 * array[15] + 1 * array[16] == 1861'

array = [Int(f'array[{i}]') for i in range(18)]

constraints = [eval(x) for x in expr.split(' && ')]

s = Solver()
s.add(*constraints)
assert s.check() == sat
m = s.model()
result = ''.join(chr(m[c].as_long()) for c in array)
print(result)
