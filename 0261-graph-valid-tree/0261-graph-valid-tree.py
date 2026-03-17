class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #an empty graph is considered a tree
        #In graph theory, a tree is defined as a connected acyclic undirected graph, so we model each edge in both directions in the adjacency list."

        if n == 0:
            return True

        if len(edges) != n-1:#"A tree with n nodes must have exactly n−1 edges. If there are more edges, a cycle exists. If there are fewer edges, the graph must be disconnected. So we check this first."
            return False

        #adj list
        adj = defaultdict(list)

        for a,b in edges: #O(E) time and O(V+E) space
            adj[a].append(b)
            adj[b].append(a)

        VISITING = 1
        UNVISITED = 0
        VISITED = 2

        visited = [UNVISITED]*n

        def dfs(node, prev): #O(V+E) space(V)

            state = visited[node]

            if state == VISITED:
                return True
            if state == VISITING:
                return False #We have already fully explored this node before, and we already know there is no cycle in the path starting from it. So we don’t need to explore it again.”

            visited[node] = VISITING

            for nei in adj[node]:
                if nei == prev:#avoid false cycle detection. Since this is an undirected graph, every edge appears twice in the adjacency list. When we traverse from a node to its neighbor, that neighbor will also have an edge back to the node we came from. If we don't ignore that edge, DFS would think we've found a cycle. So we skip the parent node (prev) to avoid falsely detecting a cycle.
                    continue
                elif not dfs(nei, node):
                    return False #we are coming back to a node which we are currently visiting indicating a cycle we came back to a node that is still in the current DFS path.

            visited[node] = VISITED
            return True


        return dfs(0,-1) and all(state == VISITED for state in visited)    