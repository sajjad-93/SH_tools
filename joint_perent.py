import maya.cmds as mc
sel=mc.ls(sl=True)
for i in range(len(sel)):
    mc.parent(sel[i],sel[i+1])