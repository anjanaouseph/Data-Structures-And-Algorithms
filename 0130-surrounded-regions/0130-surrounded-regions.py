class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        #add the surrounding 0s to queue and do BFS and mark as T

        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and ( i in [0, m-1] or j in [0, n-1] ): #boundary edges
                    queue.append((i,j))
                    board[i][j] = 'T'

        def bfs(queue):
            while queue:
                r,c = queue.popleft()

                for dR,dC in directions:
                    row = r+dR
                    col = c+dC

                    if 0<=row<m and 0<=col<n and board[row][col] == 'O':
                        queue.append((row,col))
                        board[row][col] = 'T' #neighbor of boundary 0 so we cant capture them

        bfs(queue)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
                        

# TC: O(M*N)
# SC: O(M*N)