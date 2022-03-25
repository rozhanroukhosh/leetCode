#413. Arithmetic Slices
#link https://leetcode.com/problems/arithmetic-slices/

class Solution:
    count = 0
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if(n<3): return 0
        i = 0
        while i+2 < n:
            j=i
            if(nums[j+2]-nums[j+1]==nums[j+1]-nums[j]):
                self.count+=1
                j+=3
                while(j<n and nums[j]-nums[j-1]==nums[j-1]-nums[j-2]):
                        self.count+=1
                        j+=1
            i+=1
        return(self.count)