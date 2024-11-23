# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()

        count = 0 #find the length of the LL

        curr = head

        while curr:
            count += 1
            curr = curr.next

        #node to be deleted is count-n from the begining

        curr = head

        if count == 1:
            return None

        curr = dummy
        curr.next = head
        count += 1

        for i in range(0,count-n-1):
            curr = curr.next

        curr.next =curr.next.next

        return dummy.next

        


        
        