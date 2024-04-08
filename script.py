import bpy, mathutils, math

bpy.ops.object.mode_set(mode='EDIT')   

    
for key_bones in bpy.context.object.data.edit_bones:
    if key_bones.name.find("left") != -1:
        key_bones.name = key_bones.name.replace(" left", "")	
        key_bones.name = key_bones.name + " left"
    if key_bones.name.find("right") != -1:
        key_bones.name = key_bones.name.replace(" right", "")
        key_bones.name = key_bones.name + " right"

for key_bones in bpy.context.object.data.edit_bones:
    if key_bones.name.find(" L") != -1:
        key_bones.name = key_bones.name.replace(" L", "")	
        key_bones.name = key_bones.name + " L"
    if key_bones.name.find(" R") != -1:
        key_bones.name = key_bones.name.replace(" R", "")
        key_bones.name = key_bones.name + " R"
        
for key_bones in bpy.context.object.data.edit_bones:
    if key_bones.name[0] == "l":
        key_bones.name = key_bones.name.replace("l", "", 1)	
        key_bones.name = key_bones.name + ".l"
    if key_bones.name[0] == "r":
        key_bones.name = key_bones.name.replace("r", "", 1)
        key_bones.name = key_bones.name + ".r"
        
for key_bones in bpy.context.object.data.edit_bones:
    if key_bones.name.find("L_") != -1:
        key_bones.name = key_bones.name.replace("L_", "")	
        key_bones.name = key_bones.name + " L"
    if key_bones.name.find("R_") != -1:
        key_bones.name = key_bones.name.replace("R_", "")
        key_bones.name = key_bones.name + " R"
        
for key_bones in bpy.context.object.data.edit_bones:
    if key_bones.name.find("-L") != -1:
        key_bones.name = key_bones.name.replace("-L", "")	
        key_bones.name = key_bones.name + " L"
    if key_bones.name.find("-R") != -1:
        key_bones.name = key_bones.name.replace("-R", "")
        key_bones.name = key_bones.name + " R"
        
bpy.ops.object.posemode_toggle()
