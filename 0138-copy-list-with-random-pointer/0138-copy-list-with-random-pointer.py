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

        #map the current nodes to their newly created equivalents
        while curr:
            node = Node(curr.val)
            map[curr] = node
            curr = curr.next

        curr = head

        while curr:
            map[curr].next = map[curr.next] if curr.next else None
            map[curr].random = map[curr.random] if curr.random else None
            curr = curr.next

        return map[head]

        


        