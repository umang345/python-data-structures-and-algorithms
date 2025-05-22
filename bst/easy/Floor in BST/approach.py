from os import *
from sys import *
from collections import *
from math import *


def floorInBST(root, X):

    if root is None:
        return inf
    
    if root.data == X:
        return X
    
    if root.data<X:
        rightRes = floorInBST(root.right,X)
        if rightRes<=X:
            return rightRes
        return root.data
    else:
        return floorInBST(root.left,X)