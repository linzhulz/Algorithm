class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def findMax(root):
    if root.value == None:
        return None

    v = root.value

    if root.left != None or root.right != None:
        vl = findMax(root.left)
        vr = findMax(root.right)
        v = max(vl, vr)



