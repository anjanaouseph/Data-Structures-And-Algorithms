class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (left+right)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] > nums[mid+1]:
                right = mid

            else:
                left = mid+1

        return 0
        