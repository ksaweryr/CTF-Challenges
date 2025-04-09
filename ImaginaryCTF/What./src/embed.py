from PIL import Image

im = Image.open('what_raw.png')
shares = [Image.open(f'share_{i}.jpg').convert('1') for i in range(3)]

for y in range(im.height):
    for x in range(im.width):
        pixel = list(im.getpixel((x, y)))
        for i, s in enumerate(shares):
            channel = pixel[i]
            channel = (channel & 0xfe) | int(s.getpixel((x, y)) != 0)
            pixel[i] = channel
        im.putpixel((x, y), tuple(pixel))

im.save('what.png')

# sanity check
shares = [Image.new('1', (im.width, im.height)) for _ in range(3)]

for y in range(im.height):
    for x in range(im.width):
        pixel = list(im.getpixel((x, y)))
        for i, s in enumerate(shares):
            shares[i].putpixel((x, y), pixel[i] & 1)

for i, s in enumerate(shares):
    s.save(f'sc_{i}.png')
