from collections import deque
from typing import *

def getAlienLanguage(words, n) :
    graph = dict()
    vis, pathVis = dict(), dict()

    nodeSet = getSetOfNodes(words)
    for node in nodeSet:
        graph[node] = list()
        vis[node] = False
        pathVis[node] = False
    
    for index in range(len(words)-1):
        u,v,isEdge = getEdge(words[index], words[index+1])
        if isEdge:
            graph[u].append(v)
    
    orderStack = deque()
    for node in nodeSet:
        if not vis[node]:
            if toposort(graph, node, vis, pathVis, orderStack):
                return ""
    
    result = []
    while orderStack:
        result.append(orderStack.pop())
    
    return "".join(result)

def toposort(graph:dict, node:str,vis:dict,pathVis:dict, orderStack:deque) -> bool:
    vis[node] = True
    pathVis[node] = True
    
    for adj in graph[node]:
        if not vis[adj]:
            if toposort(graph, adj, vis, pathVis, orderStack):
                return True
        elif pathVis[adj]:
            return True
    
    pathVis[node] = False
    orderStack.append(node)
    return False
        

def getSetOfNodes(words) -> Set:
    nodes = set()
    for word in words:
        for ch in word:
            nodes.add(ch)
    
    return nodes
    
def getEdge(word1, word2) -> Tuple[int, int, bool]:
    
    length = min(len(word1), len(word2))
    
    for index in range(length):
        if word1[index] != word2[index]:
            return (word1[index], word2[index], True)
    
    return (None, None, False)