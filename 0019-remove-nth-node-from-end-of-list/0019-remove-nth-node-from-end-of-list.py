# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #2 pass solution
        #n-2 node

        if not head:
            return None

        dummy = ListNode()
        dummy.next = head
   
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
            

        node_to_be_deleted = count - n

        curr = dummy

        while node_to_be_deleted > 0:
            curr = curr.next
            node_to_be_deleted -= 1

        curr.next = curr.next.next

        return dummy.next