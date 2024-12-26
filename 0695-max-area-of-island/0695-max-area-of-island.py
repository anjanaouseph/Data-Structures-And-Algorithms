class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #4-directionallu. This means you only check if a "1" is directly above, below, to the left, or to the right of another "1" to determine if they are part of the same island.
        #8 directionally means it involves diagonally connections as well.
        #"4-directional" only considers the four main compass directions

        m,n = len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != 1:
                return
            
            grid[i][j] = 0
            nonlocal area_islands
            area_islands += 1
            dfs(i,j+1)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)



        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area_islands = 0
                    dfs(i,j)
                    max_area = max(max_area, area_islands)

        return max_area        