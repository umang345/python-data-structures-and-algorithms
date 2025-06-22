from typing import *

class Node:
    def __init__(self):
        self._children = [None]*2

    def containsNode(self, key:int) -> bool:
        return not self._children[key] is None
    
    def addNode(self,key:int):
        self._children[key] = Node()

    def getNode(self, key:int):
        return self._children[key]
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def checkBitSet(self, pos:int, num:int)->bool:
        return (1<<pos) & num
    
    def insert(self, num:int):
        node = self.root
        for pos in range(31,-1,-1):
            bit = 0
            if self.checkBitSet(pos, num):
                bit = 1
            if not node.containsNode(bit):
                node.addNode(bit)
            node = node.getNode(bit)

        return node

    def getMaxXor(self, num:int) -> int:
        node = self.root
        xor = 0
        for pos in range(31,-1,-1):
            bitNeeded = 0 if self.checkBitSet(pos,num) else 1
            if node.containsNode(bitNeeded):
                xor += (1<<pos)
            else:
                bitNeeded = 1-bitNeeded
            node = node.getNode(bitNeeded)

        return xor
            

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        offlineSet = []
        for index in range(len(queries)):
            offlineSet.append((queries[index][0], queries[index][1], index))
        
        offlineSet.sort(key=lambda x : (x[1],x[2]))
        nums.sort()
    
        currIndex = 0
        result = [-1]*len(queries)

        trie = Trie()

        for numToXor, limit, resultIndex in offlineSet:
            while currIndex < len(nums) and nums[currIndex] <= limit:
                trie.insert(nums[currIndex])
                currIndex+=1
            
            if currIndex>0:
                result[resultIndex] = trie.getMaxXor(numToXor)
        
        return result