class DLLNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.prevNode = None
        self.nextNode = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def markNodeAsLatestUsed(self, key:int, node:DLLNode):
        if self.head is None:
            raise Exception("Attempted to update an empty list")
    
        if self.head is self.tail:
            if not self.head is node:
                raise Exception("Attempt to mark a non existent node")
            return
        
        if self.head is node:
            return    

        if self.tail is node:
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
        else:
            node.prevNode.nextNode = node.nextNode
            node.nextNode.prevNode = node.prevNode
        
        node.prevNode = None
        node.nextNode = self.head
        self.head.prevNode = node
        self.head = node

    def addNewNode(self, key:int, value:int)->DLLNode:
        node = DLLNode(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prevNode = node
            node.nextNode = self.head
            self.head = node
        return node
    
    def removeLastNode(self)->int:
        keyToRem = self.tail.key
        nodeToDel = self.tail
        self.tail = self.tail.prevNode
        if self.tail is None:
            self.head = None
        else:
            self.tail.nextNode = None
        
        del nodeToDel
        return keyToRem
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity    
        self.keyNodeMap = dict()
        self.dll = DLL()

    def get(self, key: int) -> int:
        if key in self.keyNodeMap.keys():
            self.dll.markNodeAsLatestUsed(key, self.keyNodeMap[key])
            return self.keyNodeMap[key].value 
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.keyNodeMap.get(key) is None:
            if len(self.keyNodeMap)==self.capacity:
                keyDeleted = self.dll.removeLastNode()
                del self.keyNodeMap[keyDeleted]
            self.keyNodeMap[key] = self.dll.addNewNode(key, value)   
                 
        else:
            self.keyNodeMap[key].value = value
            self.dll.markNodeAsLatestUsed(key, self.keyNodeMap[key])
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
