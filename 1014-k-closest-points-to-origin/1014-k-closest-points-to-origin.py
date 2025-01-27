import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        heap = []

        for x,y in points:
            distance = math.sqrt((x-0)**2+(y-0)**2)
            heapq.heappush(heap, (-distance,x,y))
            if len(heap)>k:#we need a maxheap to pop out the largest elements
                heapq.heappop(heap) #nlogk

        return [[x,y] for d,x,y in heap]


        
#The heap property is maintained, meaning the smallest element will always be at the root of the heap. However, the heap is not a fully sorted structure. It only guarantees that the smallest element is at the root (the first element in the list), and the remaining elements only satisfy the heap property — not sorted order.
      