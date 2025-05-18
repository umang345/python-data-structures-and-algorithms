from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):

    if root is None:
        return []
    
    q = deque()
    q.append((0,root))
    hashMap = dict()

    while len(q)>0:
        currLen = len(q)
        while currLen>0:
            currLen-=1
            col, node = q.popleft()
            if hashMap.get(col) is None:
                hashMap[col] = node.val 
            if not node.left is None:
                q.append((col-1, node.left))
            if not node.right is None:
                q.append((col+1, node.right))
    
    result = []
    for key in sorted(hashMap.keys()):
        result.append(hashMap.get(key))
    
    return result

        

# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = 1
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)