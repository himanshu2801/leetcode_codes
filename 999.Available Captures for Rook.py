"""
Question...
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:



Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.
Example 2:



Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.
Solution...
"""
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        temp,x,y=0,0,0
        for i in board:
            if 'R' in i:
                y=board[temp].index('R')
                x=temp
            temp=temp+1
        count=0
        for i in range(y,len(board)):
            if board[x][i]=='B':
                break
            elif board[x][i]=='p':
                count=count+1
                break
            else:
                continue
        for i in range(x,len(board)):
            if board[i][y]=='B':
                break
            elif board[i][y]=='p':
                count=count+1
                break
            else:
                continue
        for i in range(y,0,-1):
            if board[x][i]=='B':
                break
            elif board[x][i]=='p':
                count=count+1
                break
            else:
                continue
        for i in range(x,0,-1):
            if board[i][y]=='B':
                break
            elif board[i][y]=='p':
                count=count+1
                break
            else:
                continue
        return count
        
        
