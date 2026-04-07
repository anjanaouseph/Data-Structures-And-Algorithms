import heapq

class MedianFinder:
    #here the brute force is to use an array, and re-arrange the elements in sorted order as they coome by and find median. That will be O(N) time complexity. Optimized solution is by using heaps.
    #using max heap for smaller side and min heap for right side.
    def __init__(self):
        self.max_heap, self.min_heap = [],[]

    def addNum(self, num: int) -> None:
        #add to the left side first
        heapq.heappush(self.max_heap, -num)
        #we need to check two things
        #1. if the elements in max heap is larger than right heap, pop from that and push to the min heap
        if self.max_heap and self.min_heap and (-1*self.max_heap[0] > self.min_heap[0]):#then pop from there and push to min heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))#logn
        
        #if either of the length is larger than 1, then pop and push to the other one
        #we can have one of them at a time to be greater than 1 in length to accomdate for odd case
        if len(self.max_heap) > len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap)) #logn

        if len(self.min_heap) > len(self.max_heap)+1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap)) #logn
       

    def findMedian(self) -> float:
        #won't be called on empty Data Structure as per the constraints
        if len(self.max_heap) == len(self.min_heap):#then even case
            return (-1*self.max_heap[0] + self.min_heap[0])/2 #O(1)
        
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0] #O(1)

        else:
            return -self.max_heap[0] #O(1)

#for comparison purpose use peek[0] and not pop

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time Complexity : O(logn) and O(1)
# Space Complexity : O(1) The overall space complexity is O(n) because we store all inserted elements across two heaps. The findMedian operation itself uses O(1) extra space.
# Approach	       addNum	 findMedian
# Sort on insert	O(n)	    O(1)
# Sort on query	    O(1)	    O(n log n)
# Two heaps   	    O(log n)	O(1)