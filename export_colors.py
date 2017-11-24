
bl_info = {
    "name": "Export Colors",
    "author": "Sorin Covor",
    "version": (1, 0),
    "blender": (2, 7, 9),
    "location": "View3D > Object > Export Colors",
    "description": "Exports a list with all the colors in the scene.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"
}

import bpy, sys

class ExportColors(bpy.types.Operator):  
    bl_idname = "object.move_operator"  
    bl_label = "Export Colors"  
  
    def execute(self, context):  
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
        return {'FINISHED'}

def add_object_button(self, context):
    self.layout.operator(ExportColors.bl_idname, text = "Export Colors", icon = "COLORSET_02_VEC")

def register():  
    bpy.utils.register_class(ExportColors)
    bpy.types.INFO_MT_file.prepend(add_object_button)

def unregister():
    bpy.utils.unregister_class(ExportColors)
    bpy.types.INFO_MT_file.remove(add_object_button)

if __name__ == "__main__":  
    register() 
