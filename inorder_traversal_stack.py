#!urs/bin/env python
#coding = utf-8

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Stack:
    def __init__(self, size):
        self.size = size
        self.s = [0 for _ in xrange(self.size)]
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            raise Exception('overflow')
        else:
            self.top += 1
            # print 'top after push is', self.top
            self.s[self.top] = value

    def pop(self):
        if self.top == -1:
            raise Exception('underflow')
        else:
            # print 'top before pop is', self.top
            res = self.s[self.top]
            self.top -= 1
            return res

def inorderTraversal(s, node):
    if node:
        s.push(node)
        root = node.left
    while s.top >= 0 or root != None:
        if root:
            s.push(root)
            root = root.left
        else:
            res = s.pop()
            root = res
            print res.value
            root = root.right

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.left.left.right = TreeNode(6)

node1 = TreeNode(1)
node1.right = TreeNode(2)
node1.right.right = TreeNode(3)

s = Stack(100)

inorderTraversal(s, node)
inorderTraversal(s, node1)


