from typing import List

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # Write your code here
    edges.sort(key=lambda x : x[2])

    parent = [node for node in range(n)]
    size = [0]*n 
    mst = 0

    for u,v,w in edges:
        pu, pv = findParentWithCompression(u-1, parent), findParentWithCompression(v-1, parent)
        if pu!=pv:
            mst+=w
            unionBySize(pu, pv, size, parent)

    return mst    


def findParentWithCompression(node:int, parent:List[int]) -> int:
    if parent[node] == node:
        return node 
    
    parent[node] = findParentWithCompression(parent[node], parent)
    return parent[node]

def unionBySize(node1:int, node2:int, size:List[int], parent:List[int]):
    if size[node1] >= size[node2]:
        parent[node2] = node1 
        size[node1]+=size[node2]
    else:
        parent[node1] = node2 
        size[node2]+=size[node1]