#1260. Shift 2D Grid
#https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        flatten = [n for row in grid for n in row]
        k = k % (m*n)
        newArray = flatten[-k:]+flatten[:-k]
        begin = 0
        end = n
        i = 0
        while i<m:
            grid[i] = newArray[begin:end]
            begin+=n
            end+=n
            i+=1
        return(grid)
        
                
                            