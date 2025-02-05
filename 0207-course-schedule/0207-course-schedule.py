class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return False

        adjList = defaultdict(list)

        for a,b in prerequisites:#make adj matrix
            adjList[b].append(a)

        unvisited = 0
        visited= 2
        visiting = 1

        states = [unvisited]*numCourses #state array to keep track of the states

        def dfs(node):
            state = states[node]#get the state of current node
            if state == visited: return True #The node and all its neighbors have been fully processed (i.e., no cycles detected).
            if state == visiting: return False #This indicates that we have found a cycle because we are revisiting a node currently in the stack of the DFS traversal.

            states[node] = visiting #The node is currently being processed (i.e., we have entered it but not finished exploring all its neighbors).

            for nei in adjList[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True


        for i in range(numCourses):
            if not dfs(i):#dfs returns false if cycle is detected
                return False

        return True        

    # Points to be Noted:
    # Returning True for visited:
    # If a node is already visited, it means the node and all its neighbors have been processed without detecting a   cycle. Since we are traversing a directed graph, visiting a node that has already been completed in a previous traversal is harmless and doesn't create a cycle.

    # Returning False for visiting:
    # If a node is in the visiting state, it means we are encountering it again within the same DFS call stack. This indicates a back edge, meaning a cycle has been found. We return False to signal that a cycle exists.

#     In a tree:

# The number of edges is always V - 1, which is proportional to V.
# Therefore, E ≈ V, and the time complexity simplifies to O(V) instead of O(V + E).
# In contrast, for general graphs, E can vary significantly and may be much larger than V, which is why both V and E are explicitly included in the time complexity for graph DFS.For DFS in a tree:

# Total time is O(V) + O(V - 1) = O(2V - 1) = O(V).