class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        fresh = True

        #check if there are no fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh = False
                    break

        if fresh:
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

        minutes = 0

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = 2 #make it rotten 
                makeRotten(r+1,c)
                makeRotten(r-1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
            minutes += 1

        rotten = False
        #check if there is any fresh orange remaining even after rest all are rotten
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rotten = True
                    break

        if rotten:
            return -1

        return minutes - 1        