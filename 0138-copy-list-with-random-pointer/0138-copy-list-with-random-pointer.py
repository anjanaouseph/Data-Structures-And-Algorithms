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

        hashMap = {}

        curr = head

        while curr:
            dummy = Node(curr.val, None, None)
            hashMap[curr] = dummy
            curr = curr.next

            #next and random are addresses so can't copy that now

        for old in hashMap.keys():
            hashMap[old].next = hashMap[old.next] if old.next else None
            hashMap[old].random = hashMap[old.random] if old.random else None
            #else u will get hashMap[None] throws an error.

        return hashMap[head]
        