class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break

        #if array is sorted in decreasing order, then we shud return it's ascending order
        else:
            nums.reverse()
            
            return
        swap = len(nums)-1

        while nums[swap] <= nums[pivot]:#find the nextest bigger element than pivot
            swap -= 1

        nums[pivot], nums[swap] = nums[swap],nums[pivot]

        nums[pivot+1:] = reversed(nums[pivot+1:])

        return


# TC: O(N)
# SC O(1)

#1 4 5 8 7

#1 4 7 8 5

#1 4 7 5 8
        