class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        unvisited, visiting = 0, 1

        def dfs(node, prev):   #dfs to check if cycle exists     

            if states[node] == visiting:
                return True #cycle detected

            states[node] = visiting

            for nei in adj[node]:
                if nei == prev:
                    continue
                elif dfs(nei, node):
                    return True

            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

            states = [unvisited] * (len(edges) + 1)
            
            if dfs(a, -1):
                return [a,b]