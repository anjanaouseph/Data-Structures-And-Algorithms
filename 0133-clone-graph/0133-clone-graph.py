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
        if not node:
            return None

        hashMap = {}

        start = node
        stack = [node]
        visited = set()

        visited.add(node)

        while stack:
            node = stack.pop()
            #create a new node
            hashMap[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        for old,new in hashMap.items():
            for nei in old.neighbors:
                hashMap[old].neighbors.append(hashMap[nei])

        return hashMap[start]      