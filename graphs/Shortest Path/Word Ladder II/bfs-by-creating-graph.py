#User function Template for python3
from collections import deque
from math import *

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        
        queue = deque()
        queue.append((startWord,[startWord]))
        
        dis = dict()
        for word in wordList:
            dis[word] = inf
        
        dis[startWord] = 1
        
        result = []
        
        while queue:
            word,currList = queue.popleft()
            if word == targetWord:
                result.append(currList)
                continue
            
            for nextWord in wordList:
                if self.compareWords(word, nextWord) == 1:
                    if dis[word]+1 <= dis[nextWord]:
                        dis[nextWord] = dis[word]+1
                        nextList = [num for num in currList]
                        nextList.append(nextWord)
                        queue.append((nextWord, nextList))
                        
        return result
        
    def compareWords(self, w1:str, w2:str) -> int:
        
        length = min(len(w1), len(w2))
        count = 0
        
        for index in range(length):
            if w1[index]!=w2[index]:
                count+=1
                if count>1:
                    return count
        
        count+=abs(len(w1)-len(w2))
        
        return count