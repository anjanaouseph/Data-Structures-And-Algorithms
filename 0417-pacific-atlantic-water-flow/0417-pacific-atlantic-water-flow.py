class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #using multi-source bfs here 

        m = len(heights)
        n = len(heights[0])

        a_queue = deque()
        p_queue = deque()

        a_visited = set()
        p_visited = set()

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        #add first row to p queue
        for j in range(n):
            p_queue.append((0,j))
            p_visited.add((0,j))

        #add first col to p queue
        for i in range(0,m):
            p_queue.append(((i,0)))
            p_visited.add((i,0))

        #add last row to a_queue
        for j in range(0,n):
            a_queue.append((m-1,j))
            a_visited.add((m-1,j))

        #add last col to a_queue
        for i in range(0, m-1):
            a_queue.append((i,n-1))
            a_visited.add((i,n-1))

        def bfs(queue, visited):
            while queue:
                cell = queue.popleft()

                for dr,dc in directions:
                    row = cell[0] + dr
                    col = cell[1] + dc
                    if 0 <= row < m and 0<=col<n and (row,col) not in visited and heights[row][col] >= heights[cell[0]][cell[1]]:
                        visited.add((row,col))
                        queue.append((row,col))

            return visited


        return list(bfs(p_queue,p_visited).intersection(bfs(a_queue,a_visited)))