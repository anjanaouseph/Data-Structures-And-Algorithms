class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #DO BFS because we need shortest path

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        
        visited = set()

        queue = deque([(0,0)])
        visited.add((0,0))

        distance = 1 #because (0,0) part of the path

        directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),         (0, 1),     # left, right
        (1, -1), (1, 0), (1, 1)      # bottom-left, bottom, bottom-right
    ]

        def addRow(row,col):
            if row < 0 or row >= m or col<0 or col>=n or (row,col) in visited or grid[row][col] == 1:
                return
            visited.add((row,col))
            queue.append([row,col])

        while queue:
            length = len(queue)
            for _ in range(length):
                r,c = queue.popleft()

                if (r, c) == (m - 1, n - 1):
                    return distance

                for dr, dc in directions:
                    addRow(r+dr,c+dc)#checks in all 8 directions

            distance += 1
                
        return -1