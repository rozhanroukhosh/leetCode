#279. Perfect Squares
#link https://leetcode.com/problems/perfect-squares/
import math
class Solution:
    def numSquares(self, n: int) -> int:
        numlist = set()
        for i in range(1,n+1):
            if(i == math.isqrt(i) ** 2):
                numlist.add(i)
     
        que = deque()
        que.append([n,0])
        visited = set()
        while que:

            newNode, level = que.popleft()
            for j in numlist:
               
                val = newNode-j
                if(val>0 and val not in visited):
                    que.append([val,level+1])
                    visited.add(val)
                elif(val==0):
                    return level+1
                else:
                    continue
        return 0
        
                
        