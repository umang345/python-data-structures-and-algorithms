from sys import stdin,setrecursionlimit
from queue import Queue
from collections import *

setrecursionlimit(10**7)

# Binary tree node class for reference.
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

def populateParentLinks(root, parentMap):
    if root is None:
        return

    if not root.left is None:
        parentMap[root.left.data] = root 
    if not root.right is None:
        parentMap[root.right.data] = root 

    populateParentLinks(root.left, parentMap)
    populateParentLinks(root.right, parentMap)
    
def getStartNode(root, target):
    if root is None:
        return None 
    
    if root.data == target:
        return root
    
    leftNode = getStartNode(root.left, target)
    if not leftNode is None:
        return leftNode
    
    return getStartNode(root.right, target)

def timeToBurnTree(root, start):
    
    if root is None:
        return 0
    
    parentMap = dict()
    populateParentLinks(root, parentMap)
    
    myQueue = deque()
    myQueue.append(getStartNode(root,start))
    visited = set()
    timeToBurn = -1

    while len(myQueue):
        timeToBurn+=1
        currLen = len(myQueue)
        while currLen>0:
            currLen-=1
            node = myQueue.popleft()
            visited.add(node.data)
            if not node.left is None and not node.left.data in visited:
                myQueue.append(node.left)
            if not node.right is None and not node.right.data in visited:
                myQueue.append(node.right)
            if not parentMap.get(node.data) is None and not parentMap[node.data].data in visited:
                myQueue.append(parentMap[node.data])

    return timeToBurn 

# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start

#main

root, start = takeInput()

print(timeToBurnTree(root, start))