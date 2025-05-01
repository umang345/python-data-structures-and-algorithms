from sys import *
from collections import *
from math import *

def maximumSumSubarray(n, arr):

	result = None
	maxSum = -inf 
	currSum = 0
	currArr = []

	for num in arr:
		currSum+=num
		currArr.append(num)
		if currSum<num:
			currSum = num
			currArr = [num]

		if maxSum < currSum:
			maxSum = currSum
			result = list(currArr)
		elif maxSum == currSum:
			if result is None or len(result) < len(currArr):
				result = list(currArr)
			

	return result