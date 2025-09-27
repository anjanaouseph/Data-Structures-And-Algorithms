class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        box_set = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if (board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in box_set[(i//3,j//3)]):
                    return False

                else:
                    row_set[i].add(board[i][j])
                    col_set[j].add(board[i][j])
                    box_set[(i//3,j//3)].add(board[i][j])

        return True
