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
        start = node #we need to store this reference because node value gets reassigned in the below while loop
        hashMap[node] = Node(node.val)

        while stack:#create copies of all nodes first
            node = stack.pop()
            for nei in node.neighbors:
                if nei not in hashMap:
                    hashMap[nei] = Node(nei.val)
                    stack.append(nei)
                hashMap[node].neighbors.append(hashMap[nei])
            
              
        #map copies to their neighbor's copies, so iterate over hashmap
        return hashMap[start]