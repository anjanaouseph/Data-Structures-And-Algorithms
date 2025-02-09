class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        n = len(edges)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        unvisited, visiting = 0, 1

        states = [unvisited] * (n + 1)

        cycle = []

        cycle_start = -1

        def dfs(node, prev):   #dfs to check if cycle exists  
            nonlocal cycle_start   
            if states[node] == visiting:
                cycle_start = node #add start of cycle to list
                return True #cycle detected

            states[node] = visiting

            for nei in adj[node]:
                if nei == prev:
                    continue
                elif dfs(nei, node):
                    if cycle_start != -1:#include only nodes that are part of the cycle.
                        cycle.append(node)
                    if cycle_start == node: #we came back to start of cycle again 
                        cycle_start = -1 #reset cycle start
                    return True
            
            return False

        #since the graph that started as a tree from 1 to n, we do dfs for just node 1

        dfs(1,-1)

        #check if each vertex in the edges are present in the cycle, that means that edge is the culprit.
        for i in range(n-1, -1, -1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return edges[i]