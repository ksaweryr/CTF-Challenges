import pickle
from random import shuffle
import sys

flag = [(i, c) for i, c in enumerate('ictf{c0ngr4tul4t10n5_y0u_c0nv1nc3d_th3_p1ck13_t0_sh4r3_th3_fl4g}')]
shuffle(flag)


class C:
    def __reduce__(self):
        return (sys.exit, (420,), None, None, iter(flag))


print(pickle.dumps(C()).hex())
