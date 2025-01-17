class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #do binary search

        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[mid+1]:#descending slope so peak exists in the left half including mid
                right = mid
            else:
                left = mid+1 #ascneding slope maybe so peak exists in right half
            
        return left
        