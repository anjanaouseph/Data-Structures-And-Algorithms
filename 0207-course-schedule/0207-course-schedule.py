class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True #can take all course

        graph = defaultdict(list)

        #adj list
        for a,b in prerequisites:
            graph[a].append(b)

        states = [0]*numCourses

        VISITING = 1
        VISITED = 2
        UNVISITED = 0

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
# TC: O(V+E)
# SC: O(V+E)    