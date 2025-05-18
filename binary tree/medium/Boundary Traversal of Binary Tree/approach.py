class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    
    result = []
    if root is None:
        return result

    result.append(root.data) 

    leftPath, leaves, rightPath = [],[],[]

    
    getLeftPath(root.left, leftPath)
    getRightPath(root.right,rightPath)
    getLeaves(root, leaves)

    for el in leftPath:
        result.append(el)
    for el in leaves:
        result.append(el)
    for el in rightPath:
        result.append(el)

    return result

def getLeaves(root, result):
    if root is None:
        return 
    
    if root.left is None and root.right is None:
        result.append(root.data)
        return 
    
    getLeaves(root.left, result)
    getLeaves(root.right, result)

def getRightPath(root, result):
    if root is None or (root.left is None and root.right is None):
        return 
    
    if not root.right is None:
        getRightPath(root.right, result)
    else:
        getRightPath(root.left, result)
    
    result.append(root.data)

def getLeftPath(root, result):
    if root is None or (root.left is None and root.right is None):
        return
    
    result.append(root.data)
    if not root.left is None:
        getLeftPath(root.left, result)
    else:
        getLeftPath(root.right, result)
