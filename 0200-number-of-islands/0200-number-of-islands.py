class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        count = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        queue = deque()
 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    queue.append([i,j])

                    while queue:
                        cell = queue.popleft()
                        r, c = cell[0], cell[1]

                        for dR, dC in directions:
                            row, col = r+dR, c+dC
                            if row >= 0 and row <= m-1 and col >= 0 and col <= n-1 and grid[row][col] == "1":
                                queue.append([row, col])
                                grid[row][col] = "0"

        return count 

# Time complexity = O(m·n)
# Space Complexity is O(min(m·n, size of largest island)) for the queue.
