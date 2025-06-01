from typing import *
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if not len(hand)%groupSize==0:
            return False

        freq = Counter(hand)

        while freq:
            minElement = min(freq.keys())
            for index in range(groupSize):
                if freq.get(minElement+index) is None:
                    return False
                freq[minElement+index]-=1
                if freq[minElement+index] == 0:
                    del freq[minElement+index]
        
        return True