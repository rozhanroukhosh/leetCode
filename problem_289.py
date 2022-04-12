#289. Game of Life
#link https://leetcode.com/problems/game-of-life/
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        locations = [(-1,-1),(-1,0),(-1,+1),(0,-1),(0,+1), (+1,-1),(+1,0),(+1,+1)]
        newlist = []
        for i in range(m):
            for j in range(n):
                neighbourSum = 0
                for indexs in locations:
                    if(0<=i+indexs[0]<m and 0<=j+indexs[1]<n):
                        neighbourSum+=board[i+indexs[0]][j+indexs[1]]
                if(board[i][j]==1 and 2<=neighbourSum<=3 ):        
                        newlist.append(1)
                elif(neighbourSum==3 and board[i][j]==0 ):
                    newlist.append(1)
                else:
                    newlist.append(0)
        begin = 0
        end = n
        for i in range(m):
            board[i]=newlist[begin:end]
            begin+=n
            end+=n

        
                