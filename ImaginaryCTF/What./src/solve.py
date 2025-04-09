from PIL import Image


def read_block(im, x, y, s=6):
    x *= s
    y *= s
    return [im.getpixel((x + dx, y + dy)) for dx in range(s) for dy in range(s)]


src = Image.open('what.png')
dst = Image.new('1', (src.width // 6, src.height // 6))

for y in range(dst.height):
    for x in range(dst.width):
        block = read_block(src, x, y)
        combined_lsbs = [(p[0] & p[1] & p[2]) & 1 for p in block]
        dst.putpixel((x, y), int(any(combined_lsbs)))

dst.save('output.png')
