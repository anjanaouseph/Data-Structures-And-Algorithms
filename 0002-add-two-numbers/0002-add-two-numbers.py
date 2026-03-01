# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l2:
            return l1

        #but its said both nodes are not empty so ignore prev conditions

        carry = 0
        sum = 0

        dummy = ListNode()

        curr = dummy

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = (v1+v2+carry)
            sum = total%10
            carry = total//10

            Node = ListNode(sum)
            curr.next = Node
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next        