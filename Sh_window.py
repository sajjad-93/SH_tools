import maya.cmds as cmds
window = "windowUI"
if cmds.window("windowUI", ex = True):
    cmds.deleteUI(window)
sh_window = cmds.window("windowUI",t="SH",wh=(200,120))
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Jnt Drw None',c = ("drawStyle()") )
cmds.button( label='Jnt Drw Bone',c = ("drawStyleBone()") )
cmds.button( label='End Jnt Zero',c = ("endJntzero()") )
cmds.button( label='Dope CV',c = ("dispCV()") )
cmds.button( label='Dope CV Off',c = ("dispCVOff()") )
cmds.showWindow(sh_window)

def dispCV():
    crv = cmds.ls(sl=True)
    for each in crv:
        cmds.setAttr(each + "Shape.dispCV", 1)
        

def drawStyle():
    jnt = cmds.ls(sl=True)
    for each in jnt:
        cmds.setAttr(each + ".drawStyle", 2)
        
        
def drawStyleBone():
    jnt = cmds.ls(sl=True)
    for each in jnt:
        cmds.setAttr(each + ".drawStyle", 0)
        
        
        
def endJntzero():
    end_jnt = cmds.ls(sl=True)
    for each in end_Jnt:
        cmds.setAttr(each + ".jointOrientX", 0)
        cmds.setAttr(each + ".jointOrientY", 0)
        cmds.setAttr(each + ".jointOrientZ", 0)
        
        
def dispCVOff():
    import maya.cmds as cmds
    crv = cmds.ls(sl=True)
    for each in crv:
        cmds.setAttr(each + "Shape.dispCV",0)        
