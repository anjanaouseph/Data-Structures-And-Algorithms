import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        #build a heap of size k
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0] 