from typing import List
from collections import deque

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    
    if root is None:
        return root 

    queue = deque()
    queue.append((0, root))
    hashMap = dict()

    while len(queue)>0:
        currLen = len(queue)
        while currLen>0:
            currLen-=1
            col, node = queue.popleft()
            hashMap[col] = node.data 
            if not node.left is None:
                queue.append((col-1, node.left))
            if not node.right is None:
                queue.append((col+1, node.right))
    
    result = []
    for key in sorted(hashMap.keys()):
        result.append(hashMap[key])
    
    return result