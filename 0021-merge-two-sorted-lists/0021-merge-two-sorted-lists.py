# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()#dummy node is used to handle the edge cases
            curr = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    curr = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = list2
                    list2 = list2.next

            #if both or either are Null
            curr.next = list1 if list1 else list2 #point to list1 if list1 exist
            #else point to list2

            return dummy.next




        