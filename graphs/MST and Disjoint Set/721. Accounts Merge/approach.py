from typing import *

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        hashMap = dict()
        n = len(accounts)
        parent = [node for node in range(n)]
        for acIndex, account in enumerate(accounts):
            for index in range(1, len(account)):
                it = account[index]
                if hashMap.get(it) is None:
                    hashMap[it] = acIndex
                else:
                    currParent = self.findParent(acIndex, parent)
                    parent[currParent] = self.findParent(hashMap[it], parent)
        
        merged = dict()

        for key, val in hashMap.items():
            parentVal = self.findParent(val, parent)
            if merged.get(parentVal) is None:
                merged[parentVal] = []
            
            merged[parentVal].append(key)
        
        result = []
        for key, val in merged.items():
            val.sort()
            name = accounts[key][0]
            mergedList = [name]
            for v in val:
                mergedList.append(v)
            
            result.append(mergedList)
        
        return result

    def findParent(self, node:int, parent:List[int]):
        if node == parent[node]:
            return node
        
        parent[node] = self.findParent(parent[node], parent)
        return parent[node]