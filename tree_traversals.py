#! urs/bin/env python
# coding = utf-8

class TreeNode:
    def __init_(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorderPrint(root):
    if root:
        inorderPrint(root.left)
        print root.value
        inorderPrint(root.right)

def preorderPrint(root):
    if root:
        print root.valuess
        inorderPrint(root.left)
        inorderPrint(root.right)

def postorderPrint(root):
    if root:
        inorderPrint(root.left)
        inorderPrint(root.right)
        print root.value

