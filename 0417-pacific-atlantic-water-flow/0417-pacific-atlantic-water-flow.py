from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m,n = len(heights), len(heights[0])

        #for pacific ocean
        p_que = deque()
        p_seen = set()

        #for atlantic ocean
        a_que = deque()
        a_seen = set()

        #add the first row to pacific ocean set
        for i in range(n):
            p_que.append([0,i])
            p_seen.add((0,i))

        #add the first column except the first cell because we added it before
        for i in range(1,m):
            p_que.append([i,0])
            p_seen.add((i,0))

        #add the last row to atlantic ocean set
        for i in range(n):
            a_que.append([m-1,i])
            a_seen.add((m-1,i))

        #add the last column except the last cell because we added it in before step
        for i in range(0,m-1):
            a_que.append([i,n-1])
            a_seen.add((i,n-1))

        def get_coords(que, seen):
            while que:
                i,j = que.popleft()
                for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                    r,c = i+i_off, j+j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        que.append([r,c])
                        seen.add((r,c))
            return seen

        p_coords = get_coords(p_que,p_seen)
        a_coords = get_coords(a_que,a_seen)


        return list(p_coords.intersection(a_coords))





        