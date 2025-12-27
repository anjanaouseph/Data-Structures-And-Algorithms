class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #since array is sorted, the answers are found in straight contiguous block

        low = 0
        high = len(nums)-1
        result = [-1, -1]

        #left half BS

        while low <= high:
            mid = low + (high - low)//2

            if target == nums[mid]:
                result[0] = mid
                high = mid-1 #check for next one in left side

            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        #Do BS in right half
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high - low)//2

            if target == nums[mid]:
                result[1] = mid
                low = mid+1 #check for next one in left side

            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1

        return result if result else [-1,-1]