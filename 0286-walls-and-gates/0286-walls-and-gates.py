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
#First elements in queue will have distance 0 #gates 
#next set which we are adding in addRoom() will have their distance incremented by 1.    

# Python follows a top-to-bottom execution model, which means:
# Code is parsed and executed line by line in the order it appears.
# Functions must be defined before they are called.
# Variables must be assigned before they are used.

# BFS from Empty Rooms – Inefficient Approach
# Start a new BFS for every empty room (INF).
# For each empty room:
# BFS could potentially explore the entire grid to find the nearest gate.
# In the worst case, every empty room could scan all cells.
# Worst-Case Time Complexity:
# There are O(m × n) empty rooms. Worse case scenario is all cells are empty rooms
# So Each BFS can visit O(m × n) cells. O((m×n)×(m×n))=O((m×n)^2)
