from collections import deque
from math import *

class Solution:
	def wordLadderLength(self, beginWord, endWord, wordList):
		#Code here
		dis = dict()
        for word in wordList:
            dis[word] = inf
        
        dis[beginWord] = 1
        queue = deque()
        queue.append(beginWord)

        while queue:
            word = queue.popleft()
            if word == endWord:
                return dis[word]
            for nextWord in wordList:
                if self.compareWords(word, nextWord) == 1:
                    if dis[word]+1 < dis[nextWord]:
                        dis[nextWord] = dis[word]+1
                        queue.append(nextWord)
        
        return 0
	
	def compareWords(self, w1:str, w2:str) -> int:
        length = min(len(w1), len(w2))
        count = 0
        for index in range(length):
            if w1[index]!=w2[index]:
                count+=1
                if count>1:
                    return count
        
        return count+abs(len(w1)-len(w2))