# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

        
        
        
# Time Complexity: O(N)
# Space Complexity: O(N)