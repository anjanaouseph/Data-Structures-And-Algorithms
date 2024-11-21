# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head #only one node or no node

        newHead = self.reverseList(head.next)
        
        temp = head.next
        temp.next = head
        head.next = None

        return newHead
        