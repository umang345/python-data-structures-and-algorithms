from sys import *
from collections import *
from math import *

from typing import *

class Node:
    def __init__(self):
        self._children = [None]*26
        self._flag = False
    
    def containsNode(self, char:str):
        index = ord(char) - ord('a')
        return not self._children[index] is None 
    
    def getNode(self, char:str):
        index = ord(char) - ord('a')
        return self._children[index]

    def addNode(self,char:str):
        index = ord(char) - ord('a')
        self._children[index] = Node()
    
    def setFlag(self):
        self._flag = True
    
    def isFlagSet(self):
        return self._flag

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word:str):
        root = self.root 
        for ch in word:
            if not root.containsNode(ch):
                root.addNode(ch)
            root = root.getNode(ch)
        
        root.setFlag()
    
    def checkIfAllPrefixPresent(self, word:str)->bool:
        root = self.root 
        for ch in word:
            if not root.containsNode(ch):
                return False
            root = root.getNode(ch)
            if not root.isFlagSet():
                return False
        
        return True

def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    for word in a:
        trie.insert(word)
    
    result = None 
    for word in a:
        if trie.checkIfAllPrefixPresent(word):
            if result is None or len(word) > len(result):
                result =word
            elif len(word) ==  len(result) and word<result:
                result =word 
    
    if result is None:
        result = "None"
    
    return result