#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n = len(dist)
		inf = 1e8
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            if dist[i][k]!=inf and dist[k][j]!=inf and dist[i][k]+dist[k][j] < dist[i][j]:
		                dist[i][j] = dist[i][k]+dist[k][j]
		
        # Checking for negative cycles
        
        for i in range(n):
            if dist[i][i]<0:
                raise Exception("Negative cycle present")