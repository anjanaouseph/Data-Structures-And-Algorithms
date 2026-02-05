# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k <= 1:
            return head

        curr = head
        count = 0

        dummy = ListNode()
        dummy.next = head
        k_tail = dummy

        while curr:
            kth_node = self.find_kth(curr, k)

            if not kth_node:
                break

            next_node = kth_node.next
            kth_node.next = None #else it will reverse everything till end of LL

            reversed_head = self.reverse(curr)

            curr.next = next_node

            if curr == head:
                dummy.next = reversed_head
            else:
                k_tail.next = reversed_head

            k_tail = curr
            curr = next_node

        return dummy.next
    
    def reverse(self,head):
        prev = None

        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def find_kth(self,curr, k):

        count = 0

        while curr:
            count += 1

            if count == k:
                return curr
            
            curr = curr.next
        return None
