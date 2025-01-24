import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #using two pointers

        if len(nums) == 0:
            return 0

        prefix_sum = defaultdict(int)
        count = 0
        current_sum = 0
        prefix_sum[0] = 1 #to handle edge case where subarray starts from index 0 or a single element array like [3] and k=3

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum-k in prefix_sum:
                count += prefix_sum[current_sum-k]

            prefix_sum[current_sum] += 1

        return count


