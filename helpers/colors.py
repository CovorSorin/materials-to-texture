import bpy
import random

D = bpy.data

width = 16
height = 16

image_object = D.images.new(name='picOut', width=width, height=height)
num_pixels = len(image_object.pixels)

def grid(x,y):
    # we have 10 x 10 grid, list will contain total of it
    origList = []
    for i in range(width * height):
        origList.append(i)
    
    splitList = [origList[i:i+width] for i in range(0,len(origList),width)]
  
    return splitList[y][x]

def drawPixel(x,y, R, G, B):
    # multiplied by four because of r, g, b, a pattern
    pixelNumber = grid(x,y) * 4
    
    # this is a quick way to iterate
    image_object.pixels[pixelNumber] = R
    image_object.pixels[pixelNumber+1] = G
    image_object.pixels[pixelNumber+2] = B
    image_object.pixels[pixelNumber+3] = 1.0
    
    print(pixelNumber)

size = 4

def drawRectangle(x1, y1, R, G, B):
    for x in range(x1, x1 + size):
        for y in range(y1, y1 + size):
            drawPixel(x,y, R, G, B)
        
    
drawRectangle(0,0,1, 1, 0.5)

drawRectangle(0,4, 1,0.5,0.5)
drawRectangle(4,4,1, 0.5, 1)

drawRectangle(4,0,0.5, 1, 1)
