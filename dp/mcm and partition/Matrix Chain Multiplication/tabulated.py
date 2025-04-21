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
	cache = [[0 for col in range(n)] for row in range(n)]
	
	for start in range(n-1,0,-1):
		for end in range(start, n):
			if start==end:
				continue
			minOps = None
			for k in range(start, end):
				currOps = cache[start][k] + cache[k+1][end] + (arr[start-1]*arr[k]*arr[end])
				if minOps is None or minOps > currOps:
					minOps = currOps
			cache[start][end] = minOps
	return cache[1][n-1]