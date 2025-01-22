class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        
        visited = set()

        queue = deque([(0,0)])
        visited.add((0,0))

        distance = 1 #because (0,0) part of the path

        def addRow(row,col):
            if row < 0 or row >= m or col<0 or col>=n or (row,col) in visited or grid[row][col] == 1:
                return
            visited.add((row,col))
            queue.append([row,col])

        while queue:
            length = len(queue)
            for i in range(length):
                r,c = queue.popleft()

                if (r, c) == (m - 1, n - 1):
                    return distance

                addRow(r+1,c+1) #diagonal right bottom
                addRow(r+1,c-1) #diagonal left bottom
                addRow(r-1,c-1) #diagonal left top
                addRow(r-1,c+1) #diagonal right top
                addRow(r,c+1)
                addRow(r,c-1)
                addRow(r-1,c)
                addRow(r+1,c)
            distance += 1
                
        return -1