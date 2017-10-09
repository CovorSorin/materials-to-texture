import bpy
import bmesh

# doesn't work properly with separate meshes

def moveFace():
	area = bpy.context.area.type
	bpy.context.area.type = 'IMAGE_EDITOR'
	bpy.ops.uv.select_all(action = 'TOGGLE')
	bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), constraint_axis = (False, False, False), constraint_orientation = 'GLOBAL', mirror = False, proportional = 'DISABLED', proportional_edit_falloff = 'SMOOTH', proportional_size = 1)
	bpy.ops.transform.translate(value = (1, 1, 0), constraint_axis = (False, False, False), constraint_orientation = 'GLOBAL', mirror = False, proportional = 'DISABLED', proportional_edit_falloff = 'SMOOTH', proportional_size = 1)
	bpy.context.area.type = area
	bpy.ops.uv.select_all(action = 'TOGGLE')
	
def unwrap(obj):
	bpy.ops.object.mode_set(mode = 'EDIT')         
	obj = bpy.context.object                  
	me  = obj.data
	bm = bmesh.from_edit_mesh(me)        
	for face in bm.faces:
		if face.material_index == 1:
			face.select = True
			# move to the correct position
			moveFace()
			face.select = False
		me.update()

for obj in bpy.data.objects:
	if obj.type == 'MESH':
		bpy.context.scene.objects.active = obj
		bpy.ops.mesh.uv_texture_add()
		bpy.ops.object.editmode_toggle()
		bpy.ops.uv.smart_project(island_margin = 0.4)
		unwrap(obj)
