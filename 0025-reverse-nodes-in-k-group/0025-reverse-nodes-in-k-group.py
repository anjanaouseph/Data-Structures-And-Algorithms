# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:#while curr not None
            kth_node = self.getkthNode(curr,k)
            print("kth node :", kth_node)

            if not kth_node:  # if there are fewer than k nodes left
                if prev:
                    prev.next = curr  # connect the last group as is
                break  # exit the loop as no more full groups can be reversed

            next_node = kth_node.next #save the node after kth node
            kth_node.next = None

            self.reverse_k_nodes(curr)

            #check if this is the first group of reversal
            if curr == head:
                head = kth_node
                print("head", head)
            else:
                prev.next = kth_node
                print("prev.next",prev.next)

            prev = curr
            print("prev:",prev)
            curr = next_node
            print("curr:", curr)

        return head


    def getkthNode(self,curr,k):#curr advances to 2 other nodes if k=2
        while curr and k>1:
            curr = curr.next
            k -= 1
        return curr #if no k nodes then this will be None

    def reverse_k_nodes(self,curr):
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
