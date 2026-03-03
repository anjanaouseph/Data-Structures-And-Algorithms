class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0 #so that if array is full of negative no.s then only the biggest negative no will be the max sum

        return max_sum