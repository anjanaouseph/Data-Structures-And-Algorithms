"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        if not node:
            return None

        def dfs(node):

            if node in hashMap:
                return hashMap[node]

            copy = Node(node.val)
            hashMap[node] = copy

            for v in node.neighbors:
                copy.neighbors.append(dfs(v))
            return copy

        return dfs(node)


        