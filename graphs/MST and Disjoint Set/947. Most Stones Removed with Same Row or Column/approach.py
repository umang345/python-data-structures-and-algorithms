from typing import *
from typing import *

class DisjointSet:
    def __init__(self, n:int):
        self.size = [1]*n
        self.rank = [0]*n
        self.parent = [node for node in range(n)]
    
    def findParent(self, node:int) ->int :
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self,node1:int, node2:int):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
            elif self.rank[p1]<self.rank[p2]:
                self.parent[p1]=p2 
            else:
                self.parent[p2]=p1
                self.rank[p1]+=1
    
    def unionBySize(self, node1:int, node2:int):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        if p1!=p2:
            if self.size[p1]>=self.size[p2]:
                self.parent[p2]= p1
            else:
                self.parent[p1]= p2

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        
        maxRow, maxCol = 0,0
        for x,y in stones:
            maxRow = max(maxRow,x)
            maxCol = max(maxCol,y)
        
        ds = DisjointSet(maxRow+maxCol+2)
        stoneSet = set()
        for x,y in stones:
            ds.unionBySize(x, maxRow+y+1)
            stoneSet.add(x)
            stoneSet.add(maxRow+y+1)
        
        compCount = 0
        for stone in stoneSet:
            if ds.findParent(stone)==stone:
                compCount+=1
        
        return len(stones) - compCount