# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()

        behind = ahead = dummy #ahead and behind pointers pointing to dummy

        dummy.next = head

        #move the ahead point to n+1 node from dummy

        for _ in range(n+1):
            ahead = ahead.next

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next