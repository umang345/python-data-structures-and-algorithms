from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        for index in range(len(strs[0])):
            currentChar = strs[0][index]

            for s in strs:
                if index>=len(s) or s[index]!=currentChar:
                    return "".join(prefix)
            
            prefix.append(currentChar)
        
        return "".join(prefix)