import maya.cmds as cmds

selected_objects = cmds.ls(sl=True)
cmds.select(selected_objects[0])
history = cmds.listHistory(selected_objects[0])
skin_cluster = None
for node in history:
    if cmds.nodeType(node) == 'skinCluster':
        skin_cluster = node
        break
joints = cmds.skinCluster(skin_cluster, q=True, inf=True)
cmds.select(joints)
cmds.select(selected_objects[1], add=True)
cmds.SmoothBindSkin()
cmds.select(selected_objects[0])
cmds.select(selected_objects[1], add=True)
cmds.copySkinWeights(noMirror=True, sa='closestPoint', ia='oneToOne', nr=True)