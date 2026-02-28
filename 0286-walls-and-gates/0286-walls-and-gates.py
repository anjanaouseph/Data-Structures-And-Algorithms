class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        queue = deque()

        directions = [(1,0), (0,1), (-1,0), (0,-1)]


        #add the gates to the queue

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j,0))

        def bfs(queue):
            while queue:
                size = len(queue)
                for i in range(size):
                    r,c,d = queue.popleft()

                    for dR,dC in directions:
                        row = r+dR
                        col = c+dC
                        if 0<=row<m and 0<=col<n and rooms[row][col] == 2147483647:
                            rooms[row][col] = d+1
                            queue.append((row,col, d+1))

        bfs(queue)   

#Time Complexity O(m*n)
#Space Complexity O(m*n)  