class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #validate rows
        for i in range(9):
            sett = set() #initialize a set fo every row
            for j in range(9):
                if board[i][j] in sett:
                    return False

                elif board[i][j] != ".":
                    sett.add(board[i][j])

        #validate cols
        for i in range(9):
            sett = set()
            for j in range(9):
                if board[j][i] in sett:
                    return False

                elif board[j][i] != ".":
                    sett.add(board[j][i])


        #validate boards
        directions = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]

        for x,y in directions:
            sett = set() #reset after every board
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j] in sett:
                        return False

                    elif board[i][j] != ".":
                        sett.add(board[i][j])

        return True