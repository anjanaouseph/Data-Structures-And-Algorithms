# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return

        curr = headA
        lengthA = 0

        while curr:
            lengthA += 1
            curr = curr.next

        lengthB = 0
        curr = headB

        while curr:
            lengthB += 1
            curr = curr.next

        if lengthA > lengthB:#B is smaller
            slow = headB

            diff = lengthA - lengthB

            fast = headA
            for i in range(diff):
                fast = fast.next
        else: #A is smaller or both equal
            slow = headA
            diff = lengthB - lengthA
            fast = headB

            for i in range(diff):
                fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow        