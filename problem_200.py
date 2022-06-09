#200. Number of Islands
#link https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def bfs(i,j):
            if(i>=m or i<0 or j>=n or j<0):
                return
            else:
                if(grid[i][j]=='0'):
                    return
                else:
                    grid[i][j]='0'
                    bfs(i+1,j) 
                    bfs(i-1,j) 
                    bfs(i,j+1) 
                    bfs(i, j-1)
                    return
         
        count=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=='1'):
                    count+=1
                    bfs(i,j) 
        return count
