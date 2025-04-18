class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        front = s
        back = "".join(list(reversed(s)))
        cache = [0 for colIndex in range(n+1)]
        
        for index1 in range(1, n+1):
            tempCache = [0 for colIndex in range(n+1)]
            for index2 in range(1,n+1):
                if front[index1-1]==back[index2-1]:
                    tempCache[index2] = 1+cache[index2-1]
                else:
                    tempCache[index2] = max(
                        cache[index2-1],
                        max(
                            tempCache[index2-1],
                            cache[index2]
                        )
                    )
            
            for cacheIndex in range(n+1):
                cache[cacheIndex] = tempCache[cacheIndex]

        return n - cache[n]