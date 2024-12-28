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

        #iterative DFS
        if not node:
            return None

        hashMap = {}

        stack = [node]
        start = node

        while stack:#create copies of all nodes first
            node = stack.pop()
    
            copy = Node(node.val)
            hashMap[node] = copy
            for nei in node.neighbors:
                    if nei not in hashMap:
                        stack.append(nei)
            
              
        #map copies to their neighbor's copies, so iterate over hashmap

        for old, new in hashMap.items():
            for nei in old.neighbors:
                new.neighbors.append(hashMap[nei])

        return hashMap[start]