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

        while fast and fast.next:#fast can go till none
            slow = slow.next #increment slow by 1
            fast = fast.next.next #increment fast by 2

            #now we got the LL divided into 2 halves, slow.next is the first element of 2nd half.
        second = slow.next #second pointer starts from first element of the second part
        prev = slow.next = None #setting end of first half as None because we are splitting the linkedlist

        while second:#inplace reversal
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #Now first half points to head
        #Second half head is at prev
        #just reassign second to point to prev
        first = head
        second = prev

        while second:#since second will be the shorter list if nodes are odd.
            temp1 = first.next #save the links which we are going to cut
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        #since both linkedlist ends with a None, the resultant will have None in the end anyways.