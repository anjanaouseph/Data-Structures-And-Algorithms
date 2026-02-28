class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        #add the surrounding 0s to queue and do BFS and mark as T

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c):
            if r < 0 or r>m-1 or c<0 or c>n-1 or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'
            
            for dR,dC in directions:
                row = r+dR
                col = c+dC
                dfs(row,col)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and ( i in [0, m-1] or j in [0, n-1] ): #boundary edges
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
                        

# TC: O(M*N)
# SC: O(M*N)