class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not len(nums):
            return -1

        l, r = 0, len(nums)-1

        #traditional BS
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid+1

            else:
                r = mid - 1

        return -1