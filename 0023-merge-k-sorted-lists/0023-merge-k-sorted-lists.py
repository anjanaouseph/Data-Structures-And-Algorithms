# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #since there are more than two or k LL we need to use a heap. Else follow merge two sorted LLs solution.

        heap = []

        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists): #o(k)
            if node:
                heapq.heappush(heap, (node.val, i, node)) #we push the head of each LL not all elements. so K elements at a time in heap., we need node value to get next element

        while heap: #loop runs exactly N times.
            val, i, node = heapq.heappop(heap) 
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return dummy.next    