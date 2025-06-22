class Node:
    def __init__(self):
        self.__children = [None]*26
        self.__flag = False
    
    def containsKey(self,char:str):
        index = ord(char)-97
        return self.__children[index]!=None

    def addKey(self, char:str):
        index = ord(char)-97
        self.__children[index] = Node()
    
    def getNode(self, char:str):
        index = ord(char)-97
        return self.__children[index]
    
    def setFlag(self):
        self.__flag = True
    
    def isFlagSet(self):
        return self.__flag

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if not temp.containsKey(ch):
                temp.addKey(ch)
            temp = temp.getNode(ch)
        
        temp.setFlag()

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            if not temp.containsKey(ch):
                return False
            temp = temp.getNode(ch)
        
        return temp.isFlagSet()
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            if not temp.containsKey(ch):
                return False
            temp = temp.getNode(ch)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)