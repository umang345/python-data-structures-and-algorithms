from typing import List
from collections import deque

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    traversal = []
    visited = [False]*n

    queue = deque()
    queue.append(0)

    while queue:
        popped = queue.popleft()
        if visited[popped]:
            continue
        visited[popped] = True
        traversal.append(popped)
        for neighbour in adj[popped]:
            queue.append(neighbour)
    
    return traversal