#!urs/bin/env python
# coding = utf-8

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(root):
    '''
    :param root: the root of the binary tree
    :return: the maximum height of a binary tree
    '''
    if root == None:
        return 0
    else:
        heightl = height(root.left)
        heightr = height(root.right)
        if heightl > heightr:
            return heightl + 1
        else:
            return heightr + 1

def printGivenLevel(root, level):
    if root == None:
        return
    if level == 1:
        print root.value
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

def traversal_level_order(root):
    h = height(root)
    for level in range(1, h + 1):
        printGivenLevel(root, level)






