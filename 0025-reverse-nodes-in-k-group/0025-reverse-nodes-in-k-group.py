# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        curr = head
        k_tail = dummy
        dummy.next = curr

        while curr:
            #find kth node
            kth_node = self.find_kth_node(curr, k)

            if not kth_node:
                k_tail.next = curr #just join the remaining nodes without reversing
                break

            next_node = kth_node.next
            kth_node.next = None #do this else reverse function will reverse everything in the LL till the end. So cut the LL here.

            reversed_head = self.reverse(curr)

            if curr == head: #only for first node we do this
                new_head = reversed_head #(or kth_node)
                dummy.next = new_head
            else:
                k_tail.next = reversed_head
                
            k_tail = curr
            curr = next_node

        return dummy.next


    def find_kth_node(self, curr, k):
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, curr):
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev