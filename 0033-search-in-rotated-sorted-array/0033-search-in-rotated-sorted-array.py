class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right)//2

            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:#we are in left sorted array
                if target > nums[mid] or target < nums[left]:
                    left = mid+1
                else:
                    right = mid-1 #target < nums[mid] or target > nums[left] or (target < nums[mid] and
                    #target < nums[left])


            else: #we are in right sorted array
                if target < nums[mid] or target > nums[right]:
                    right = mid-1
                else:
                    left = mid+1 #target > nums[mid] or target < nums[right]

        return -1