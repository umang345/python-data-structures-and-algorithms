from math import *

def floorSqrt(n):
   if n==0:
      return 0
      
   low, high = 1,n
   result = -inf

   while low<=high:
      mid = low + (high-low)//2
      if mid*mid <=n:
         if mid>result:
            result = mid 
         low = mid+1
      else:
         high = mid-1
   
   return result

n= int(input())
print(floorSqrt(n))