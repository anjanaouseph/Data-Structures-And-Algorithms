import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        heap = []

        for point in points:
            distance = math.sqrt((point[0]-0)**2+(point[1]-0)**2)
            heapq.heappush(heap, (-distance, [point[0],point[1]]))
            if len(heap)>k:#we need a maxheap to pop out the largest elements
                heapq.heappop(heap) #nlogk

        res = []

        for element in heap: 
            res.append(element[1])

        return res


        
#The heap property is maintained, meaning the smallest element will always be at the root of the heap. However, the heap is not a fully sorted structure. It only guarantees that the smallest element is at the root (the first element in the list), and the remaining elements only satisfy the heap property — not sorted order.
      