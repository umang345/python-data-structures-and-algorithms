def floorSqrt(n):
   root = 1
   while root*root <n:
      root+=1
   
   if root*root > n:
      root-=1
   
   return root 



n= int(input())
print(floorSqrt(n))



'''
TC -> O(root(n))
'''