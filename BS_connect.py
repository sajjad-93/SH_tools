import maya.cmds as mc

bs = "BLEND_SHAPE"
blend_attr = mc.listAttr(bs, m = 1, k = 1)
blend_attr.pop(0)
print (blend_attr)
for blends in blend_attr:
    attr=mc.addAttr("Expressions_ctrl",ln=(blends),dv = 0 ,max = 1,min=0,k=1)
    print (attr)
    mc.connectAttr(("Expressions_ctrl."+blends),(bs+"."+blends))