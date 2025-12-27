class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low < high:
            if nums[low] <= nums[high]: #when there is only one element or its a sorted array in asc
                return nums[low] 

            mid = low + (high - low)//2

            #check neighbors
            if (mid == 0 or nums[mid] < nums[mid-1]) and (mid == len(nums)-1 or nums[mid] < nums[mid+1]): #handle OOB condition also
                return nums[mid] #we found the min element

            #else we go to the unsorted half to find the min element.
            if nums[low] <= nums[mid]:
                low = mid+1
            else:
                high = mid
        return nums[low]