class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        visited_a = set()
        visited_p = set()

        #we need to do a BFS

        queue_a = deque()
        queue_p = deque()

        #add first col to pacific ocean
        for i in range(m):
            queue_p.append((i,0))
            visited_p.add((i,0))

        #first row add
        for j in range(1,n):
            queue_p.append((0,j))
            visited_p.add((0,j))

         #add last col to atlantic ocean
        for i in range(m):
            queue_a.append((i,n-1))
            visited_a.add((i,n-1))

        #last row add
        for j in range(0,n-1):
            queue_a.append((m-1,j))
            visited_a.add((m-1,j))

        directions = [(-1, 0), (1,0), (0,-1), (0, 1)]

        def bfs(queue, visited):
            while queue:
                i, j = queue.popleft()
                for dx, dy in directions:
                    rx,ry = dx+i, dy+j
                    if 0<=rx<m and 0<=ry<n and (rx,ry) not in visited and heights[i][j]<= heights[rx][ry]:
                        queue.append((rx,ry))
                        visited.add((rx,ry))

        bfs(queue_a,visited_a)
        bfs(queue_p,visited_p)

        return list(visited_a.intersection(visited_p))

                 
        


        


        


        