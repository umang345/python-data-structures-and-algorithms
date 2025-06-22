from typing import *

class Node:
    def __init__(self):
        self._children = [None]*2

    def containsNode(self, node):
        return not self._children[node] is None
    
    def addNode(self, node):
        self._children[node] = Node()

    def getNode(self, node):
        return self._children[node]

class Trie:
    def __init__(self):
        self.root = Node()

    def checkBitSet(self,pos:int, num:int) -> bool:
        return ((1<<pos) & num) != 0
    
    def insert(self, num:int):
        node = self.root
        for index in range(31,-1,-1):
            bit = 0
            if self.checkBitSet(index, num):
                bit = 1
            if not node.containsNode(bit):
                node.addNode(bit)
            node = node.getNode(bit)

    def getMaxXor(self, num:int) -> int:
        xor = 0
        node = self.root
        for index in range(31,-1,-1):
            bitNeeded = 0 if self.checkBitSet(index,num) else 1
            if node.containsNode(bitNeeded):
                xor += (1<<index)
            else:
                bitNeeded = 1-bitNeeded
            node = node.getNode(bitNeeded)
        
        return xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        xor = 0
        for num in nums:
            xor = max(xor,trie.getMaxXor(num))
        
        return xor