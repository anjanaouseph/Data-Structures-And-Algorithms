"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        map = {}

        curr = head

        while curr:
            node = Node(x=curr.val)
            map[curr] = node
            curr = curr.next

        curr = head

        while curr:
            node = map[curr]
            node.next = map[curr.next] if curr.next else None
            node.random = map[curr.random] if curr.random else None
            curr = curr.next

        return map[head]  