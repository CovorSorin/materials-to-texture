import bpy, sys

fo = open("colors.csv", "w")

materials = bpy.data.materials

for material in materials:
    r = int(round(material.diffuse_color.r * 255))
    g = int(round(material.diffuse_color.g * 255))
    b = int(round(material.diffuse_color.b * 255))
    fo.write(str(r) + ',' + str(g) + ',' + str(b) + '\n');

fo.close()
