import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k  = k
        self.nums = nums
        heapq.heapify(self.nums) #O(N)
        while len(self.nums)>k:
            heapq.heappop(self.nums) #O(N-K*O(N))
        

    def add(self, val: int) -> int:
    #When we use self.nums.append(val), the value is simply added to the list without maintaining the heap property. This means that after appending, the list is no longer a valid min-heap, and any subsequent heap operation will be inefficient. Forces heap to reorder after pop (less efficient). So use heappush instead.
        
        heapq.heappush(self.nums, val) #O(logK)

        if len(self.nums)>self.k:
            heapq.heappop(self.nums) # O(log k)

        return self.nums[0] # O(1)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)