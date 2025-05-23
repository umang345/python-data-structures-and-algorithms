'''
Find value per weight and sort the array
'''

from os import *
from sys import *
from collections import *
from math import *

def maximumValue(items, n, w):

	perUnitWeightPairs = []
	for pair in items:
		perUnitWeightPairs.append((pair[1]/pair[0], pair))
	
	perUnitWeightPairs.sort(key=lambda x : x[0], reverse=True)

	weightAvl = w
	result = 0
	index = 0
	while weightAvl > 0 and index < n:
		if perUnitWeightPairs[index][1][0] <= weightAvl:
			result+=perUnitWeightPairs[index][1][1]
			weightAvl-=perUnitWeightPairs[index][1][0]
		else:
			result+=weightAvl*perUnitWeightPairs[index][0]
			break
		index+=1

	return result

