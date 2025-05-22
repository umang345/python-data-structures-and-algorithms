from math import *

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def largestBST(root):
    res,_,_ = helper(root)
    return res

def helper(root) -> tuple:
    if root is None:
        return (0, -inf, inf)
    
    leftMaxBST, leftMax, leftMin = helper(root.left)
    rightMaxBST, rightMax, rightMin = helper(root.right)

    isCurrBST = root.data > leftMax and root.data < rightMin
    currMax = max(root.data, max(leftMax, rightMax))
    currMin = min(root.data, min(leftMin, rightMin))

    if isCurrBST:
        return (1+leftMaxBST+rightMaxBST, currMax, currMin)
    else:
        return (max(leftMaxBST, rightMaxBST), inf, -inf) 