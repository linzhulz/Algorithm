#!usr/bin/env python
#coding = utf-8

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
