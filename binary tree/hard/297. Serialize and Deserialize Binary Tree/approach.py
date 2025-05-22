# Definition for a binary tree node.
from collections import *

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serializeHelper(self, root, serializedArr):
        if root is None:
            serializedArr.append('#')
            serializedArr.append(',')
            return
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            currLen = len(queue)
            while currLen>0:
                currLen-=1
                node = queue.popleft()
                if not node is None:
                    serializedArr.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    serializedArr.append('#')
                serializedArr.append(',')
        return

    def serialize(self, root):
        '''
        [1,2,3,#,#,4,5,#,#,#,#]
        '''
        serializedArr = []
        self.serializeHelper(root,serializedArr)
        return "".join(serializedArr[:-1])

    def deserializeHelper(self, data):
        
        deserializedArr = data.split(',')
        if deserializedArr[0]=='#':
            return None

        queue = deque()
        index = 0
        head = TreeNode(int(deserializedArr[index]))
        queue.append(head)

        while len(queue)>0 and index<len(deserializedArr)-1:
            currLen = len(queue)
            while currLen>0:
                currLen-=1
                node = queue.popleft()
                index+=1
                if deserializedArr[index]!='#':
                    node.left = TreeNode(int(deserializedArr[index]))
                    queue.append(node.left)
                index+=1
                if deserializedArr[index]!='#':
                    node.right = TreeNode(int(deserializedArr[index]))
                    queue.append(node.right)
        
        return head
    
    def deserialize(self, data):
        return self.deserializeHelper(data)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))





























