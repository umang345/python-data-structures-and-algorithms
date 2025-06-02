def dfsCycleCheck(node,parent, visited, graph) -> bool:
    if visited[node]:
        return True 
    
    visited[node] = True 

    for neighbour in graph[node]:
        if neighbour!=parent:
            if dfsCycleCheck(neighbour, node, visited, graph):
                return True 
    
    return False
        

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
            if dfsCycleCheck(node,-1, visited, graph):
                return "Yes"
    
    return "No"