class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        visited = [UNVISITED]*n

        #in this case even if cycle is present that's okay
        def dfs(node):

            visited[node] = VISITED

            for nei in adj[node]:
                if visited[nei] != VISITED:
                    dfs(nei)

            
        count = 0

        for i in range(n):
            if visited[i] != VISITED:
                count += 1
                dfs(i)

        return count