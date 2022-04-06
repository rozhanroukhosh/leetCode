#118. Pascal's Triangle
#link https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l= [[1] for x in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,i):
                l[i].append((l[i-1][j-1]+l[i-1][j]))
            l[i].append(1)
        return l
                
                
        