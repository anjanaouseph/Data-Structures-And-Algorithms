class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(i, j):
            if i<0 or i>m-1 or j<0 or j>n-1 or board[i][j]!= 'O':
                return
            board[i][j] = 'T'
            for dx, dy in directions:
                dfs(i+dx, j+dy)

        #dfs the the non-surrounding regions of 'O' and make it to T
        for i in range(m):
            for j in range(n):
                #if cols and rows on the edges
                if board[i][j] == 'O' and ( i in [0, m-1] or j in [0, n-1]):
                    dfs(i,j)
        #mark everything else as 'X' capture the surrounding regions
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        #unmark all T's back to O's

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                    





