#!urs/bin/env python
# coding=utf-8

def catalan(n):
    # base case
    if n == 0:
        return 1

    # catalan(n) is the summation of catalan(i)*catalan(n-1-i)
    res = 0
    for i in range(n):
        res += catalan(i)*catalan(n - 1 - i)
    return res



