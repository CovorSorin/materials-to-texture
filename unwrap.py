import bpy
import bmesh

def unwrap(obj):
	bpy.ops.object.mode_set(mode = 'EDIT')
	bpy.ops.uv.smart_project(island_margin = 0.4)
	me  = obj.data
	bm = bmesh.from_edit_mesh(me)
	for face in bm.faces:
		if face.material_index == index:
			face.select = True
	me.update()

for obj in bpy.data.objects:
	if obj.type == 'MESH':
		unwrap(obj)


# for each face in faces
# smart uv project
# read material index
# scale (very small)
# move accordingly
