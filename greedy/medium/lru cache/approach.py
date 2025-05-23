class DLLNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.prevNode = None 
        self.nextNode = None 

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.count = 0 

    def deleteNode(self,nodeToDel):
        if self.count == 0:
            raise Exception("Attempt to delete from an empty dll")
        elif self.count == 1:
            del self.head 
            self.head, self.tail = None,None
        else:
            if nodeToDel is self.tail:
                self.tail = self.tail.prevNode
                self.tail.nextNode = None 
            elif nodeToDel is self.head:
                self.head = self.head.nextNode
                self.head.prevNode = None 
            else:
                nodeToDel.prevNode.nextNode = nodeToDel.nextNode
                nodeToDel.nextNode.prevNode = nodeToDel.prevNode
                nodeToDel.nextNode = None 
                nodeToDel.prevNode = None 
            del nodeToDel
        
        self.count-=1

    
    def addNodeAtHead(self, key, value):
        newNode = DLLNode(key, value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            newNode.prevNode = self.tail
            self.tail = self.tail.nextNode
        
        self.count+=1
        return newNode
    
    def deleteTailNode(self):
        if self.count == 1:
            del self.tail 
            self.head, self.tail = None, None 
        else:
            self.tail = self.tail.prevNode
            del self.tail.nextNode
            self.tail.nextNode = None 
        self.count-=1
    
    def getLastNodeKey(self):
        return self.tail.key




class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.keyNodeMap = dict()

    def get(self,key: int) -> int:
        if self.keyNodeMap.get(key) is None:
            return -1
        else:
            value = self.keyNodeMap[key].value
            self.dll.deleteNode(self.keyNodeMap[key])
            newNode = self.dll.addNodeAtHead(key,value)
            self.keyNodeMap[key] = newNode
            return value

    def put(self,key: int, value: int) -> int:
        if self.keyNodeMap.get(key) is None:
            if self.dll.count == self.capacity:
                del self.keyNodeMap[self.dll.getLastNodeKey()]
                self.dll.deleteTailNode()
            nodeAdded = self.dll.addNodeAtHead(key,value)
            self.keyNodeMap[key] = nodeAdded
            
        else:
            self.dll.deleteNode(self.keyNodeMap[key])
            updatedNode = self.dll.addNodeAtHead(key,value)
            self.keyNodeMap[key] = updatedNode
