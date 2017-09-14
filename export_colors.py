import bpy, sys

fo = open("colors.csv", "w")
materials = bpy.data.materials

# used for gamma correction
# gamma = 1 / 2.2 -> WINDOWS
# gamma = 1 / 1.8 -> MAC
gamma = 1 / 2.2

for material in materials:
    color = material.diffuse_color
    r = int(255 * pow(color.r, gamma))
    g = int(255 * pow(color.g, gamma))
    b = int(255 * pow(color.b, gamma))
    fo.write(str(r) + ',' + str(g) + ',' + str(b) + '\n');

fo.close()
