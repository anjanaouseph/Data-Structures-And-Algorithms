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
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #slow will land at right middle for even length

        curr = slow.next
        slow.next = None

        prev = None

        #reverse the second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        list1 = head
        list2 = prev

        while list2: #list2 will always be smaller
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2