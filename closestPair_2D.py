#!urs/bin/env python
# coding=utf-8

import numpy as np
import pandas as pd

# generate 20 pairs of (x,y) coordinates



def euclidean_dist(p, q):
    '''
    :param p: point 1
    :param q: point 2
    :return: the euclidean distance between them
    '''
    return np.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

def closestPair(points):


