class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        #check if there are no fresh oranges
        if not any(1 in row for row in grid):
            return 0

        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                    visited.add((i,j))

        def makeRotten(r,c):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or grid[r][c] == 0:
                return
            queue.append([r,c])
            visited.add((r,c))

        minutes = 0 #initial given state will be 0th minute

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = 2 #make it rotten 
                makeRotten(r+1,c)
                makeRotten(r-1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
            minutes += 1

        #check if there is any fresh orange remaining even after rest all are rotten
        if any(1 in row for row in grid):
            return -1
       
        return minutes-1 #we need to return the last minute all oranges become rotten, since after the last BFS we iterate again, we need to return minutes-1.    