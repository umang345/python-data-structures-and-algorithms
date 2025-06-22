class Node:
    def __init__(self):
        self.__children = [None]*26
        self.__prefixCount = 0

    def containsNode(self,ch:str) -> bool:
        index = ord(ch)-97
        return not self.__children[index] is None 

    def addNode(self, ch:str):
        index = ord(ch)-97
        self.__children[index] = Node()

    def getNode(self, ch:str):
        index = ord(ch)-97
        return self.__children[index]    

    def incrementPrefixCount(self):
        self.__prefixCount+=1
    
    def getPrefixCount(self):
        return self.__prefixCount

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word:str):
        root = self.root 
        for ch in word:
            if not root.containsNode(ch):
                root.addNode(ch)
            root = root.getNode(ch)
            root.incrementPrefixCount()
        
    
    def countStartsWith(self, prefix:str) -> int:
        root = self.root 
        for ch in prefix:
            if not root.containsNode(ch):
                return 0 
            root = root.getNode(ch)
        
        return root.getPrefixCount()

def longestCommonPrefix(arr, n):
    trie = Trie()
    for word in arr:
        trie.insert(word)
    
    index = 0
    while index < len(arr[0]):
        if trie.countStartsWith(arr[0][:index+1]) == n:
            index+=1
        else:
            break
    
    return arr[0][:index]



