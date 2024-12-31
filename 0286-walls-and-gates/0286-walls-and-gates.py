class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #using BFS using Queues starting from the gates.

        m,n = len(rooms), len(rooms[0])
        visited = set()
        queue = deque()

        distance = 0

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i,j]) #add coordinates of gates to the queue. queue is a deque (double-ended queue), which supports adding and removing elements efficiently. Lists ([i, j]) are mutable and are commonly used for such temporary storage and traversal.
                    visited.add((i,j)) #add them to visited set. A list ([i, j]) cannot be added to a set because lists are mutable and therefore unhashable. So we add a tuple. set requires its elements to be hashable and immutable to ensure uniqueness and efficient lookups.
        def addRoom(row, col):
            if row < 0 or row >= m or col<0 or col>=n or (row,col) in visited or rooms[row][col] == -1:
                return
            visited.add((row,col))
            queue.append([row,col])

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                #do BFS and fill the surrounding boxes
                rooms[r][c] = distance
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            distance += 1 #increment by 1        