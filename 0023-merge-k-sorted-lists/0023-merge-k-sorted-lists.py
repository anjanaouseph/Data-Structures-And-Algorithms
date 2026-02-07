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

        heap = [] #size will be k

        for i,node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val,i, node)) #O(logn)*k if there is a tie compare with index value

        dummy = ListNode(-1)

        curr = dummy

        while heap:
            node_val, idx, min_node = heapq.heappop(heap)
            curr.next = min_node

            if min_node.next is not None:
                heapq.heappush(heap,(min_node.next.val, idx, min_node.next))
            
            curr = curr.next

        return dummy.next