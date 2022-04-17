#1137. N-th Tribonacci Number
#link https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    def tribonacci(self, n: int) -> int:
        steps = [0,1,1]
        for i in range (3,n+1):
            steps.append(0)
            if i-1>0 and steps[i-1]:
                steps[i]+=steps[i-1]
            if i-2>0 and steps[i-2]:
                steps[i]+=steps[i-2]
            if i-3>0 and steps[i-3]:
                steps[i]+=steps[i-3]
            
        return steps[n]