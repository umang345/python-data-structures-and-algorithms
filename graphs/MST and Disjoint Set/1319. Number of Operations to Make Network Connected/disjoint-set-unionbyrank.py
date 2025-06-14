from typing import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections)<n-1:
            return -1
        parent = [node for node in range(n)]
        rank = [0]*n
        
        for u,v in connections:
            pu = self.findParent(u, parent)
            pv = self.findParent(v, parent)
            if pu!=pv:
                self.unionByRank(pu, pv, rank, parent)
        
        count = -1
        for index, val in enumerate(parent):
            if index == val:
                count+=1
        
        return count

    def unionByRank(self, node1:int,node2:int, rank:List[int], parent: List[int]):
        if rank[node1] > rank[node2]:
            parent[node2] = node1 
        elif rank[node1] < rank[node2]:
            parent[node1] = node2 
        else:
            parent[node2] = node1 
            rank[node1]+=1



    def findParent(self, node:int, parent:List[int]) -> int:
        if parent[node] == node:
            return node 
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]