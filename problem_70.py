#70. Climbing Stairs
#link https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2,3]
        for i in range (3,n):
            steps.append(0)
            if i-1>0 and steps[i-1]:
                steps[i]+=steps[i-1]
            if i-2>0 and steps[i-2]:
                steps[i]+=steps[i-2]
            
        return steps[n-1]