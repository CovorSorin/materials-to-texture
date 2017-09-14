import PIL
from PIL import Image, ImageDraw

file_name = 'colors.csv'
colors = []

with open(file_name,'r') as fo:
    for line in fo:
        line = line.split(',')
        line = list(map(int, line))
        colors.append(tuple(line))

size = 64

tiles_x = 4
tiles_y = 4
tiles = tiles_x * tiles_y

if (tiles < len(colors)):
	print("Not enought tiles for all the colors")
	
img = Image.new('RGB', (tiles_x * size, tiles_y * size), (255, 255, 255))
draw = ImageDraw.Draw(img)

index = 0

for y in range(0, tiles_y):
    y = y * size
    for x in range(0, tiles_x):
        x = x * size
        if (index < len(colors)):
            draw.rectangle(((x, y), (size + x, size + y)), fill = colors[index])
        else:
            draw.rectangle(((x, y), (size + x, size + y)), fill = "white")
        index = index + 1

img.save("uv.png")
