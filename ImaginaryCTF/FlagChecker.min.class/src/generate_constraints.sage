from z3 import *

flag = 'ictf{asm_but_java}'

assert len(flag) == 18

values = [ord(c) for c in flag[5:-1]]
chars = [Int(f'chars[{i + 5}]') for i in range(12)]


def gen(coeffs):
    lhs = []
    rhs = 0

    for i, c in enumerate(coeffs):
        if c != 0:
            lhs.append(int(c) * chars[i])
            rhs += int(c) * values[i]

    return lhs, int(rhs)


cm = random_matrix(ZZ, 12)
assert cm.column_space().dimension() == 12

equations = [gen(row) for row in cm.rows()]
constraints = [sum(lhs) == rhs for (lhs, rhs) in equations]

s = Solver()
s.add(*constraints)
assert s.check() == sat

m = s.model()

# from IPython import embed; embed()

result = ''.join(chr(m[c].as_long()) for c in chars)
assert 'ictf{' + result + '}' == flag

repr = ' || '.join(' + '.join(str(term) for term in lhs) + ' != ' + str(rhs) for lhs, rhs in equations)
print(repr)
