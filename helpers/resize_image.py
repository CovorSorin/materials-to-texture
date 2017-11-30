from PIL import Image
import sys

name = sys.argv[1]

size = 1024, 1024
im = Image.open(name)
im = im.resize(size, resample = 0)
im.save(name, "PNG")
