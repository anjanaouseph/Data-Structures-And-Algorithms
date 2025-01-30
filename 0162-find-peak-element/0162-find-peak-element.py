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


# The loop condition left < right ensures that the last iteration stops before mid + 1 would go out of bounds:
# If left == right, the loop terminates, so nums[mid + 1] is never accessed when mid == len(nums) - 1.

# Why Boundary Checks Are Necessary
# To Avoid Index Out of Bounds Errors

# When mid == 0, there is no nums[mid - 1], so attempting to access it would cause an out-of-bounds error.
# When mid == len(nums) - 1, there is no nums[mid + 1], so accessing it would also cause an out-of-bounds error.
# To Handle Boundary Conditions Correctly

# The peak could occur at the edges of the array (nums[0] or nums[len(nums) - 1]), and these cases must be handled explicitly.
# For example:
# If nums[0] > nums[1], then nums[0] is a peak.
# If nums[len(nums) - 1] > nums[len(nums) - 2], then nums[len(nums) - 1] is a peak.