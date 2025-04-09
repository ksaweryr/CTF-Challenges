import os

asm_code = '''
.class public forge
.super java/lang/Object

.method public static check : ([B)Z
    .code stack 1 locals 1
        {}
    .end code
.end method

.end class
'''

with open('forge.j', 'wt') as f:
    f.write(asm_code.format('pop\n' * 6 + 'nop\n' * 990))

os.system('krak2 asm --out forge.class forge.j')

with open('code', 'rb') as f:
    bytecode = f.read()

with open('forge.class', 'rb') as f:
    template = f.read()

output = template.replace(b'\x57' * 6 + b'\x00' * 990, bytecode)

with open('forge.class', 'wb') as f:
    f.write(output)
