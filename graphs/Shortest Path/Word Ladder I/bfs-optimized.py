from collections import deque

class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		
		words = set([w for w in wordList])
		
		queue = deque()
		queue.append((startWord,1))
		
        while queue:
		    word, tfm = queue.popleft()
			
            if word == targetWord:
		        return tfm
		    
		    for index, char in enumerate(word):
		        for ch in range(ord('a'), ord('z')+1):
		            if chr(ch)!=char:
		                newWord = word[:index]+chr(ch)+word[index+1:]
		                if newWord in words:
		                    queue.append((newWord, tfm+1))
		                    words.remove(newWord)
		
		return 0