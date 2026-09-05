class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:



        board=[[""]*3 for i in range(3)]

        
        for i in range(len(moves)):
            r,c=moves[i]

            if i%2==0:
                board[r][c]="A"

            else:
                board[r][c]="B"


        for row in board:
            if row[0]==row[1]==row[2] !="":
                return row[0]


        for c in range(3):
            if board[0][c]==board[1][c]==board[2][c]!="":
                return board[0][c]


        if board[0][0]==board[1][1]==board[2][2]!="":
            return board[0][0]

        if board[0][2] ==board[1][1]==board[2][0]!="":
            return board[0][2]

        
        if len(moves)==9:
            return "Draw"

        return "Pending"


        