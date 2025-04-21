from os import *
from sys import *
from collections import *
from math import *

def matrixMultiplication(arr, n):
	'''
	[10 15 20 25]
	[0  1  2  3 ]
	M[i] = A[i-1]*A[i]
	i->k and k+1->j   (i <= k <j)
	'''
	return helper(1, n-1, arr)

def helper(start, end, arr):
	if start == end:
		return 0

	minOperations = None

	for k in range(start, end):
		currOps = helper(start,k,arr) + helper(k+1, end,arr) + (arr[start-1]*arr[k]*arr[end])
		if minOperations is None or minOperations > currOps:
			minOperations = currOps

	return minOperations

	