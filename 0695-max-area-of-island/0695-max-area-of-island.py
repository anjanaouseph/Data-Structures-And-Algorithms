class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        max_count = 0
        count = [0]

        dir = [(1,0), (0,1), (0,-1), (-1,0)]

        def dfs(r,c):
            if r<0 or r>m-1 or c<0 or c>n-1 or grid[r][c] != 1:
                return

            grid[r][c] = 0
            count[0] += 1

            for dR, dC in dir:
                dfs(r+dR, c+dC)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    max_count = max(max_count, count[0])
                    count[0] = 0

        return max_count
        