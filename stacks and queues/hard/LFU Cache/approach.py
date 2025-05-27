class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextNode = None
        self.prevNode = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.keyNodeMap = dict()
    
    def removeNode(self, key:int) -> DLLNode:
        node = self.keyNodeMap[key]

        if node is self.tail:
            return self.removeNodeAtTail()
        
        elif node is self.head:
            self.head = self.head.nextNode
            self.head.prevNode = None
            node.nextNode = None
        
        else:
            node.prevNode.nextNode = node.nextNode
            node.nextNode.prevNode = node.prevNode

        del self.keyNodeMap[node.key]
        return node
    
    def removeNodeAtTail(self) -> DLLNode:
        nodeToDel = self.tail
        self.tail = self.tail.prevNode
        if not self.tail is None:
            self.tail.nextNode = None
        else:
            self.head = None
        nodeToDel.prevNode = None
        del self.keyNodeMap[nodeToDel.key]
        return nodeToDel

    def addExistingNodeAtHead(self, node:DLLNode):
        self.keyNodeMap[node.key] = node
        node.prevNode = None
        node.nextNode = None
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = self.head.prevNode


    def addNewNodeAtHead(self,key,value)-> DLLNode:
        node = DLLNode(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nextNode = self.head
            self.head.prevNode = node
            self.head = self.head.prevNode
        self.keyNodeMap[key] = node
        return node
    
    def __len__(self):
        return len(self.keyNodeMap)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.minFrequency = 1
        self.keyFreqMap = dict()
        self.freqDllMap = dict()

    def get(self, key: int) -> int:
        cacheResult = -1
        if key in self.keyFreqMap.keys():
            currFreq = self.keyFreqMap[key]
            currDll = self.freqDllMap[currFreq]
            currNode = currDll.removeNode(key)
            cacheResult = currNode.value
            if len(currDll)==0 and self.minFrequency == currFreq:
                self.minFrequency = currFreq+1
                del self.freqDllMap[currFreq]
                del currDll
            
            currFreq+=1
            if not currFreq in self.freqDllMap.keys():
                self.freqDllMap[currFreq] = DLL()
            
            currDll = self.freqDllMap[currFreq]
            currDll.addExistingNodeAtHead(currNode)
            self.keyFreqMap[key] = currFreq
        
        return cacheResult
            

    def put(self, key: int, value: int)  -> None:
        if not self.keyFreqMap.get(key) is None:
            currFreq = self.keyFreqMap[key]
            currDll = self.freqDllMap[currFreq]
            currNode = currDll.removeNode(key)
            currNode.value = value

            if len(currDll)==0 and self.minFrequency == currFreq:
                self.minFrequency = currFreq+1
                del self.freqDllMap[currFreq]
                del currDll
            
            currFreq+=1
            if not currFreq in self.freqDllMap.keys():
                self.freqDllMap[currFreq] = DLL()
            
            currDll = self.freqDllMap[currFreq]
            currDll.addExistingNodeAtHead(currNode)
            self.keyFreqMap[key] = currFreq
        
        else:
            
            if len(self.keyFreqMap) < self.capacity:
                self.keyFreqMap[key] = 1
                self.minFrequency = 1
                if self.freqDllMap.get(1) is None:
                    self.freqDllMap[1] = DLL()
                self.freqDllMap[1].addNewNodeAtHead(key, value)
            else:
                nodeRemoved = self.freqDllMap[self.minFrequency].removeNodeAtTail()
                del self.keyFreqMap[nodeRemoved.key]
                nodeRemoved.key = key
                nodeRemoved.value = value
                self.keyFreqMap[key]=1
                self.minFrequency = 1
                if self.freqDllMap.get(1) is None:
                    self.freqDllMap[1] = DLL()
                self.freqDllMap[self.minFrequency].addExistingNodeAtHead(nodeRemoved)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
