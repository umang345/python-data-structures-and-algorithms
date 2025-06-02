from collections import deque

def cycleDetection(edges, n, m):

    graph = []
    for _ in range(n):
        graph.append([])
    
    for edge in edges:
        graph[edge[0]-1].append(edge[1]-1)
        graph[edge[1]-1].append(edge[0]-1)

    visited = [False]*n

    for node in range(n):
        if not visited[node]:
            if detectCycleInComponent(graph, n, node,visited):
                return "Yes"

    return "No"
    


def detectCycleInComponent(graph,n,node, visited)->bool:

    queue = deque()
    queue.append((node,-1))

    while queue:
        node, parent = queue.popleft()
        if visited[node]:
            return True
        visited[node] = True 
        for neighbour in graph[node]:
            if neighbour!=parent:
                queue.append((neighbour, node))
        
    return False