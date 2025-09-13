class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums)-1

        #first find the min element
        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[right]:
                #unsorted half
                left = mid+1

            else:
                right = mid

        min_element = left

        #do BS again 
        if nums[min_element] == nums[0]:
            left, right =0,  len(nums)-1
        elif target >= nums[min_element] and target >= nums[0]:
            left, right = 0, min_element-1
        else:
            left, right = min_element, len(nums)-1

        while left<=right:
            mid = (left + right)//2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return -1 