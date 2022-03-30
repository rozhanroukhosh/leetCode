#74. Search a 2D Matrix
#link https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i<len(matrix):
            if(target>=matrix[i][0] and target<= matrix[i][-1]):
                if target in matrix[i]:
                    return True
                else:
                    return False
            i+=1
        return False