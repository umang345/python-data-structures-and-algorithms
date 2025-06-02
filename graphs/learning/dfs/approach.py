from typing import *

def dfsHelper(node,graph, dfsTraversal, visited)->None:
    if visited[node]:
        return 
    visited[node] = True 
    dfsTraversal.append(node)
    for neighbour in graph[node]:
        dfsHelper(neighbour, graph, dfsTraversal, visited)
        

def depthFirstSearch(V: int, E: int, edges: List):
    
    graph = []
    for node in range(V):
        graph.append([])
        
    for edge in edges:
        listEdge = list(edge)
        u,v = listEdge[0], listEdge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # for node in range(V):
    #     graph[node].sort()

    result = []
    visited = [False]*V 
    for node in range(V):
        if not visited[node]:
            dfsTraversal = []
            dfsHelper(node,graph, dfsTraversal, visited)
            dfsTraversal.sort()
            result.append(dfsTraversal)
    
    return result 
    
    
