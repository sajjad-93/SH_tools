import maya.cmds as mc
attr=mc.ls(sl=1)
for i in attr:
    mc.addAttr(ln="MeshDisplay",at ="enum",en="Normal:Templete:Reference:",k=True)
    mc.addAttr(ln="FacialCtrlVis",at ="bool",k=True)
    
    
mc.connectAttr ('Main.MeshDisplay', 'Geometry.overrideDisplayType')
mc.connectAttr ('Main.MeshDisplay', 'Geometry.overrideEnabled')
mc.connectAttr ("Main.FacialCtrlVis","FaceMotionSystem.visibility")