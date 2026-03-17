class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)

        n = len(edges)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        VISITED = 2
        UNVISITED = 0
        VISITING = 1

        nodes = [UNVISITED]*(len(edges)+1)

        result = set()
        cycle_start = [-1]

        def dfs(node, prev):

            state = nodes[node]

            if state == VISITED:
                return True

            if state == VISITING:
                cycle_start[0] = node
                return False

            nodes[node] = VISITING

            for nei in adj[node]:
                if nei == prev:
                    continue

                elif not dfs(nei, node):
                    if cycle_start[0] != -1:
                        result.add(node)
                    
                    if cycle_start[0] == node:
                        cycle_start[0] = -1                
                    return False

            nodes[node] = VISITED

            return True

        dfs(1,0)

        for i in range(n-1,-1,-1):
            if edges[i][0] in result and edges[i][1] in result:
                return edges[i]

        return [-1,-1]