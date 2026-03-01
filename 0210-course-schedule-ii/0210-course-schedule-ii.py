class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

# We’re given courses and prerequisite pairs.
# This is a dependency problem because some courses must be taken before others.
# Whenever we have items with dependencies, we can model them as a directed graph.
# Each course is a node, and a prerequisite pair [a, b] means we draw a directed edge b → a (b must be taken before a).
# The question asks whether we can finish all courses.
# Since courses have prerequisites that must be taken before them, we need to find an ordering of courses that respects these dependencies. This is exactly a topological ordering. A topological ordering exists if and only if the directed graph has no cycles.
# So the problem reduces to detecting a cycle in a directed graph.
# DFS with visiting states, or
# BFS using Kahn’s algorithm (topological sort).

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        graph = defaultdict(list) #adj list

        for a,b in prerequisites: #Each node maps to the nodes it has edges to.
            graph[a].append(b)

        result = []

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [0]*numCourses

        def dfs(i):
            state = states[i]

            if state == VISITED:
                return True #We have already fully explored this node before, and we already know there is no cycle in the path starting from it. So we don’t need to explore it again.”
            
            if state == VISITING:
                return False #cycle detected

            states[i] = VISITING #we are coming back to a node which we are currently visiting indicating a cycle e came back to a node that is still in the current DFS path.

            for nei in graph[i]:
                if not dfs(nei):
                    return False

            states[i] = VISITED
            result.append(i)

            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result  
        
    # TC: O(V+E)
    # SC: O(V+E)