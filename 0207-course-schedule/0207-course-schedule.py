class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        graph = defaultdict(list)

        VISITED = 2
        UNVISTED = 0
        VISITING = 1

        states = [UNVISTED]*numCourses

        for a,b in prerequisites:
            graph[a].append(b)

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
            

        for node in range(numCourses):
            if not dfs(node):#not able to complete the dfs, means cycle detected
                return False

        return True

# TC: O(V+E)
# SC: O(V+E)
        