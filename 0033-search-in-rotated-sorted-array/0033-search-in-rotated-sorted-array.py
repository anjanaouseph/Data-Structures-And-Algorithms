class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the minimum in rotated array

        left = 0
        right = len(nums)-1

        while left<right:
            mid = left+(right-left)//2
            #we found the pivot element
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        min_element = left

        #now to find the index of the target, do another binary search

        #for already ascending non rotatd array
        if nums[0] == nums[min_element]:
            left, right = 0, len(nums)-1
        elif target >= nums[min_element] and target < nums[0]:
            left, right = min_element, len(nums)-1
        else:
            left, right = 0, min_element-1


        #do traditional BS

        while left<=right:
            mid = left + (right-left)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return -1