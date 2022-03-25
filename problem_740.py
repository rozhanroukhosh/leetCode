#740. Delete and Earn
#link https://leetcode.com/problems/delete-and-earn/
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
       nums = sorted(nums)
       n = len(nums)      
       lis = []
         
       i=0
       j=2
       while i< n:
            holder=nums[i]
            lis.append(nums[i])
            if(i>=1):         
                if(nums[i]-1!=nums[i-1]):
                    j=1
                else:
                    j=2
            if(len(lis)-j>0):
                    lis[-1]+=max(lis[0:len(lis)-j])
            
            while(i+1<n and holder==nums[i+1]):
                lis[-1]+=holder
                i+=1
            
            
            i+=1
       return(max(lis))

        
            
    
            
        
            
            
        