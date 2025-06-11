from collections import deque

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #Code here
        
        words = set([w for w in wordList])
        
        queue = deque()
        queue.append([startWord])
        if startWord in words:
            words.remove(startWord)
        result = []
        
        while queue:
            currLen = len(queue)
            wordsToRemove = set()
            while currLen>0:
                currLen-=1
                currList = queue.popleft()
                
                if currList[-1] == targetWord:
                    result.append(currList)
                    continue
                
                word = currList[-1]
                for index, char in enumerate(word):
                    for ci in range(ord('a'), ord('z')+1):
                        if chr(ci)!=char:
                            newWord = word[:index]+chr(ci)+word[index+1:]
                            if newWord in words:
                                newList = [w for w in currList]
                                newList.append(newWord)
                                wordsToRemove.add(newWord)
                                queue.append(newList)
                        
            words = words.difference(wordsToRemove)
        
        return result
                    