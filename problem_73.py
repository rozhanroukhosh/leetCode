#73. Set Matrix Zeroes
#link https://leetcode.com/problems/set-matrix-zeroes/

import numpy as np
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numMatrix = np.array(matrix)
        idx = np.argwhere(numMatrix == 0)
        for i in idx:
            matrix[i[0]] = [0]*len(matrix[0])
            for j in range(len(matrix)):
                matrix[j][i[1]]=0
        
            
                
                
                
        