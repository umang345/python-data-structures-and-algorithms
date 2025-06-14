from typing import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        edges = []
        for node in range(n):
            for adj in range(node,n):
                if isConnected[node][adj]:
                    edges.append([node, adj])
        
        parent = [node for node in range(n)]
        size = [1]*n

        for u,v in edges:
            pu, pv = self.findParentWithCompression(u, parent), self.findParentWithCompression(v, parent)
            if pu!=pv:
                self.unionBySize(pu, pv, size, parent)
        
        count = 0
        for index, val in enumerate(parent):
            if index == val:
                count+=1
        
        return count

    def unionBySize(self, node1, node2, size, parent):
        if size[node1]>=size[node2]:
            parent[node2] = node1
            size[node1]+=size[node2]
        else:
            parent[node1] = node2
            size[node2]+=size[node1]

    def findParentWithCompression(self,node:int, parent:List[int]) -> int:
        if parent[node] == node:
            return node 
        parent[node] = self.findParentWithCompression(parent[node], parent)
        return parent[node]