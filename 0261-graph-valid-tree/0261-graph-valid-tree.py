class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        #empty graph is considered a tree. Base Case no graph to traverse, so empty graph is a tree. Return True
        if not n:
            return True

        #we make adj list but its bidirectional
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        unvisited, visited, visiting = 0,2,1
        states = [unvisited]*n

        visit_set = set() 

        def dfs(node, prev):
            state = states[node]
            if state == visited: return True
            if state == visiting: return False

            states[node] = visiting

            for nei in adj[node]:
                if nei == prev:#skip for false detection of a cycle
                    continue
                elif not dfs(nei, node):
                    return False

            states[node] = visited
            visit_set.add(node)

            return True

        return dfs(0, -1) and len(visit_set)==n