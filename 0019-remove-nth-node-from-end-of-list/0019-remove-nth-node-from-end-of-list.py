# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        curr = head
        length = 0

        #find the length of the linked-list first
        while curr:
            length += 1
            curr = curr.next

        curr = dummy
        count = 0

        while curr:
            if count == length - n:
                break
            count += 1
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next


        return dummy.next
            

        




            
        