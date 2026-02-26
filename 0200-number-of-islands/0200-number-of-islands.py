class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r,c):
            #check boundary
            if r < 0 or c < 0 or r > m-1 or c > n-1 or grid[r][c] != '1':
                return
            
            grid[r][c] = 0 #flood the grid so we don't visit in next iteration or else use a seen set
            dfs(r+1, c) 
            dfs(r,c+1) 
            dfs(r-1, c)
            dfs(r, c-1)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count       