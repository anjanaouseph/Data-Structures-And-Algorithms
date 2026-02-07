# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        #merging each list one by one
        merged = None

        for list in lists:
            merged = self.merge(merged, list)

        return merged

    def merge(self,list1, list2):

        dummy = ListNode(-1)

        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1

        else:
            curr.next = list2

        return dummy.next
    

# Time Complexity: O(Nlogn) where N is no of nodes
# Space Complexity: O(N)