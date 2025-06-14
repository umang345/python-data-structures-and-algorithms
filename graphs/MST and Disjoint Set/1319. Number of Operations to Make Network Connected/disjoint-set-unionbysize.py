from typing import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections)<n-1:
            return -1
        parent = [node for node in range(n)]
        size = [1]*n
        
        for u,v in connections:
            pu = self.findParent(u, parent)
            pv = self.findParent(v, parent)
            if pu!=pv:
                self.unionBySize(pu, pv, size, parent)
        
        count = -1
        for index, val in enumerate(parent):
            if index == val:
                count+=1
        
        return count

    def unionBySize(self, node1:int,node2:int, size:List[int], parent: List[int]):
        if size[node1]>=size[node2]:
            parent[node2] = node1
            size[node1]+=size[node2]
        else:
            parent[node1] = node2
            size[node2]+=size[node1]


    def findParent(self, node:int, parent:List[int]) -> int:
        if parent[node] == node:
            return node 
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]