class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #bfs is more straightforward

        m = len(grid)
        n = len(grid[0])

        queue = deque()

        fresh_oranges = [0]
        time = [0]

        directions = [(1,0), (-1, 0), (0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j)) #at time 0 we append to queue rotten oranges

                if grid[i][j] == 1:
                    fresh_oranges[0] += 1

        if fresh_oranges[0] == 0:
            return 0 #nothing to rot

        def bfs(queue):
            while queue:
                size = len(queue)
                time[0] += 1 #at time 1 we add to queue the first set of BFS neighbors and make it rotten
                for i in range(size):
                    r,c = queue.popleft()

                    for dR, dC in directions:
                        row = r+dR
                        col = c+dC

                        if 0<=row<m and 0<=col<n and grid[row][col] == 1:
                            queue.append((row,col))
                            grid[row][col] = 2
                            fresh_oranges[0] -= 1
                            if fresh_oranges[0] == 0:
                                return time[0]


        bfs(queue)

        if fresh_oranges[0] == 0:
            return time[0] 

        return -1 #fresh orange is left so can't make everything rotten

    # TC: O(2*mn) = O(m*n)
    # SC: O(m*n)