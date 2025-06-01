from os import *
from sys import *
from collections import *
from math import *

def kMaxSumCombination(a, b, n, k):
	
	result = list()
	for num1 in a:
		for num2 in b:
			result.append(num1+num2)
	
	result.sort(reverse = True)
	return result[:k]
	