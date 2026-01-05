class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        #instead of having a dummy index we can do below
        prev = nums[0]
        curr = max(prev, nums[1])

        for i in range(2, len(nums)):
            temp = curr
            curr = max(curr, nums[i]+prev) #here we add corresponding profit and take dp two steps back to avoid adj houses.
            prev = temp

        return curr

# Time Complexity : O(N)
# Space Complexity : O(N)