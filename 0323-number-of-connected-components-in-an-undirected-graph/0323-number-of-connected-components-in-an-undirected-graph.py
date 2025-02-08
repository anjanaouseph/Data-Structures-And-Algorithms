class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0

        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        unvisited, visited = 0, 2

        states = [unvisited]*n

        visit_set = set()

        connected = 0

        def dfs(node):
            state = states[node]
            if state == visited: return

            states[node] = visited

            visit_set.add(node)

            for nei in adj[node]:
                    dfs(nei)

        for i in range(n):
            if i not in visit_set:
                dfs(i)
                connected += 1
    
        return connected
        