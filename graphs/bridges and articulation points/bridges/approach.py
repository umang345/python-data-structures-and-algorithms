from typing import *

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = []
        for _ in range(n):
            graph.append(list())
        
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)

        vis = [False]*n
        inTime = [-1]*n
        lowTime = [-1]*n
        bridgeSet = set()
        currTime = [0]

        self.findBridge(graph, vis, 0, -1, currTime, inTime, lowTime, bridgeSet)

        result = []
        for x,y in bridgeSet:
            result.append([x,y])
        
        return result
    
    def findBridge(self, graph:list, vis:list, node:int, parent:int,currTime:list,inTime:list,lowTime:list, bridges:set):

        vis[node] = True
        currTime[0]+=1
        inTime[node] = currTime[0]
        lowTime[node] = currTime[0]

        for adj in graph[node]:
            if adj!=parent:
                if not vis[adj]:
                    self.findBridge(graph, vis, adj, node, currTime, inTime, lowTime, bridges)
                
                lowTime[node] = min(lowTime[node], lowTime[adj])
                if inTime[node] < lowTime[adj]:
                    bridges.add(  (min(node, adj), max(node, adj)) )
            