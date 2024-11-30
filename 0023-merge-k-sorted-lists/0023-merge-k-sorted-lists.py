# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))#if 2 elements are same heap tries to sort based on second element which is the index here, can't give node as it throws an error. Its a memory address.
        D = ListNode()
        curr = D

        while heap:
            val,i,node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap,(node.val,i,node))

        return D.next
        