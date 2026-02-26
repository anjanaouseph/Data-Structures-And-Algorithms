class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != "1":
                return

            grid[i][j] = "0" #flood each lands
            dfs(i,j+1)#move to right
            dfs(i+1,j)#move down
            dfs(i-1,j)#move up
            dfs(i,j-1)#move left

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i,j)#to make all the connected nodes as 0

        return num_islands

        