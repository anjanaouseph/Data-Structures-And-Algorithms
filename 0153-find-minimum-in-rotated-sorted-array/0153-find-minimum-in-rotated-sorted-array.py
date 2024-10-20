class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right: #exit if just only one element in search space
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                left = mid+1 #can't set left = mid because then it will be an infinite loop if mid happens to be equal to left, the value of left will not change, potentially causing an infinite loop.
            else:
                right = mid  # not mid - 1 because mid could be the minimum
            

        return nums[left]
        
# left = mid + 1:

# This moves the search to the right half of the array, excluding mid because we know nums[mid] is greater than nums[right], indicating that the rotation point and thus the minimum value must be to the right of mid.
# right = mid:

# If nums[mid] is less than or equal to nums[right], then the mid element is a candidate for the minimum, as the elements from mid to right are sorted in increasing order (no rotation point within them). Therefore, mid could be the minimum, or it could be to the left of mid, but not to the right.

# Using left < right:
# Avoids Redundant Comparisons and Infinite Loops: Using left < right as the condition prevents the binary search from including the case where left equals right. If left equals right, it means you've narrowed down to a single element, which must be the minimum if all previous checks were correct. By stopping the loop when left equals right, you avoid unnecessary checks and potential errors in pointer management within the loop.

# left <= right:
# May end up with an infinite loop by not moving the pointers sufficiently, particularly in scenarios where mid calculates to left or right without changing their values.