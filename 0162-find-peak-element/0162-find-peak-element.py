class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #do binary search

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if mid>0 and nums[mid] < nums[mid-1]:#checking boundary mid>0 and we check if ascending so check in left half
                right = mid-1
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                left = mid+1 #descending check righ half
            else:
                return mid #we found it

        