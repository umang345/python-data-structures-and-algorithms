class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [0 for colIndex in range(len(text2)+1)]

        for index1 in range(1, len(text1)+1):
            tempCache = [0 for colIndex in range(len(text2)+1)]

            for index2 in range(1, len(text2)+1):
                if text1[index1-1] == text2[index2-1]:
                    tempCache[index2] = 1+cache[index2-1]
                else:
                    tempCache[index2] = max(
                        cache[index2-1],
                        max(
                            cache[index2],
                            tempCache[index2-1]
                        )
                    )

            for cacheIndex in range(len(text2)+1):
                cache[cacheIndex] = tempCache[cacheIndex]

        return cache[len(text2)]