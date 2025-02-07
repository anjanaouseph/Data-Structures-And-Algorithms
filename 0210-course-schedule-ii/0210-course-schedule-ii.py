class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a,b in prerequisites:
            adj[a].append(b)

        visited = 2
        visiting = 1
        unvisited = 0
        states = [unvisited]*numCourses

        order = []

        #return True if No CYCLE, False if CYCLE
        def dfs(node):
            state = states[node]
            if state == visited: return True
            if state == visiting: 
                return False

            states[node] = visiting

            for nei in adj[node]:
                  if not dfs(nei):
                    return False

            states[node] = visited
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order