# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        group_prev = dummy
        dummy.next = head

        while True:
            kth_node = self.getkthNode(group_prev,k)
            if not kth_node:
                break
            groupNext = kth_node.next
            
            #lets reverse this
            prev,curr = kth_node.next, group_prev.next #if prev is None we will break the LL
            
            while curr!=groupNext: #curr is not at the end which is groupNext
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            #Now we need to update group_prev node to kth position
            temp = group_prev.next #it pointed to 1
            group_prev.next = kth_node #kth was 2
            group_prev = temp

        return dummy.next


    def getkthNode(self,curr,k):#curr advances to 2 other nodes if k=2
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr #if no k nodes then this will be None
        