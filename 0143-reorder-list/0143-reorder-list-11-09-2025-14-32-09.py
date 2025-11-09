# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #slow pointer points to last node of first half now
        
        curr = slow.next
        prev = None
        slow.next = None #detach the first half from second half

        #now do a in-place reversal
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #head of reversed list is prev

        #now merge the two lists
        list1 = head
        list2 = prev

        dummy = ListNode()

        curr = dummy

        while list1 and list2:
            curr.next = list1
            curr = list1
            list1 = list1.next

            curr.next = list2
            curr = list2
            list2 = list2.next


        curr.next = list1 if list1 else list2

        #when we divide into two halves, list2 will be of same length or smaller. List1 will be longer or of same length as list2

        return dummy.next        