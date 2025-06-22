class Node:
    def __init__(self):
        self._children = [None]*26
        self._flag = False

    def containsNode(self,ch:str) -> bool:
        index = ord(ch) - ord('a')
        return not self._children[index] is None
    
    def addNode(self, ch:str):
        index = ord(ch) - ord('a')
        self._children[index] = Node()
    
    def getNode(self, ch:str):
        index = ord(ch) - ord('a')
        return self._children[index]
    
    def setFlag(self):
        self._flag = True
    
    def isFlagSet(self):
        return self._flag

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insertIfNotExist(self, word, startIndex:int, endIndex) -> bool:
        root = self.root 
        for index in range(startIndex,endIndex+1):
            ch = word[index]
            if not root.containsNode(ch):
                root.addNode(ch)
            root = root.getNode(ch)
        
        if root.isFlagSet():
            return False 
        
        root.setFlag()
        return True
        
def countDistinctSubstrings(s):
    # Write your code here
    count = 1
    trie = Trie()
    for startIndex in range(len(s)):
        for endIndex in range(startIndex, len(s)):
            if trie.insertIfNotExist(s, startIndex, endIndex):
                count+=1
    
    return count 