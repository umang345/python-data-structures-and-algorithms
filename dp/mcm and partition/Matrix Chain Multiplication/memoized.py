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
	cache = [[-1 for col in range(n)] for row in range(n)]
	return helper(1, n-1, arr,cache)

def helper(start, end, arr,cache):
	if start == end:
		return 0

	if cache[start][end]!=-1:
		return cache[start][end]

	minOperations = None

	for k in range(start, end):
		currOps = helper(start,k,arr,cache) + helper(k+1, end,arr,cache) + (arr[start-1]*arr[k]*arr[end])
		if minOperations is None or minOperations > currOps:
			minOperations = currOps

	cache[start][end] = minOperations
	return cache[start][end]
