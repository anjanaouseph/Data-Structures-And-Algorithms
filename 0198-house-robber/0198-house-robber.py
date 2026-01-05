class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums) #initialize a 1D array

        #instead of having a dummy index we can do below
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2]) #here we add corresponding profit and take dp two steps back to avoid adj houses.

        return dp[len(nums)-1]