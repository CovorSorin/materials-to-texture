import PIL
from PIL import Image, ImageDraw

file_name = 'colors.csv'
colors = []

with open(file_name,'r') as fo:
    for line in fo:
        line = line.split(',')
        line = list(map(int, line))
        colors.append(tuple(line))

tiles = 4
size = 64

img = Image.new('RGB', (tiles * size, tiles * size), (255, 255, 255))
draw = ImageDraw.Draw(img)

index = 0

for y in range(0, tiles):
    y = y * size
    for x in range(0, tiles):
        x = x * size
        if (index < len(colors)):
            draw.rectangle(((x, y), (size + x, size + y)), fill = colors[index])
        else:
            draw.rectangle(((x, y), (size + x, size + y)), fill = "white")
        index = index + 1

img.save("uv.png")
