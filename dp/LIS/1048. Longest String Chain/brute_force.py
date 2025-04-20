from typing import *
from functools import reduce 

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        cache = [1 for index in range(len(words))]

        wordsSorted = list(sorted(words, key=len))
        for index in range(len(wordsSorted)):
            for compare in range(index):
                if self.isPredecessor(wordsSorted[compare], wordsSorted[index]) and cache[index] <= cache[compare]:
                    cache[index] = 1+cache[compare]

        return reduce(lambda acc,x : max(acc,x), cache, cache[0])

    def isPredecessor(self, word1, word2) -> bool:
        if len(word1)!= len(word2)-1:
            return False
        
        diffCount = 0
        index1, index2 = 0,0

        while index1<len(word1) and index2<len(word2):
            if word1[index1]!=word2[index2]:
                diffCount+=1
            else:
                index1+=1
            index2+=1
        
        diffCount += (len(word1) - index1) + (len(word2) - index2)
        return diffCount==1
