from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self):
        self.__children = [None]*26
        self.__prefixCount = 0
        self.__wordCount = 0
        self.__flag = False
    
    def containsNode(self, char:str) -> bool:
        index = ord(char)-97
        return not self.__children[index] is None
    
    def addNode(self, char:str):
        index = ord(char)-97
        self.__children[index] = Node()

    def getNode(self,char:str) -> bool:
        index = ord(char)-97
        return self.__children[index]

    def incrementPrefixCount(self):
        self.__prefixCount+=1
    
    def incrementWordCount(self):
        self.__wordCount+=1
    
    def decrementPrefixCount(self):
        self.__prefixCount-=1
    
    def decrementWordCount(self):
        self.__wordCount-=1

    def getWordCount(self):
        return self.__wordCount

    def getPrefixCount(self):
        return self.__prefixCount

    def setFlag(self):
        self.__flag = True

    def unsetFlag(self):
        self.__flag = False  

    def isFlagSet(self)-> bool:
        return self.__flag



class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        root = self.root 
        for ch in word:
            if not root.containsNode(ch):
                root.addNode(ch)
            root = root.getNode(ch)
            root.incrementPrefixCount()
        
        root.setFlag()
        root.incrementWordCount()

    def countWordsEqualTo(self, word):
        root = self.root 
        for ch  in word:
            if not root.containsNode(ch):
                return 0
            root = root.getNode(ch)

        if root.isFlagSet():
            return root.getWordCount()
        
        return 0

    def countWordsStartingWith(self, word):
        root = self.root 
        for ch  in word:
            if not root.containsNode(ch):
                return 0
            root = root.getNode(ch)
        
        return root.getPrefixCount()
        

    def erase(self, word):
        root = self.root 
        for ch  in word:
            if not root.containsNode(ch):
                raise Exception("Attempted to erase a non-existent word")
            root = root.getNode(ch)
            root.decrementPrefixCount()

        root.unsetFlag()
        root.decrementWordCount()
        return 0
