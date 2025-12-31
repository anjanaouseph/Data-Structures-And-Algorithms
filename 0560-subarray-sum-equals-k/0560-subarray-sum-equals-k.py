#need hashmap to store the occurances of the sum not index here.
# We check prefix_sum - k because if the current prefix sum is prefix_sum, any earlier prefix sum equal to prefix_sum - k forms a subarray ending here with sum k

# Why NOT check prefix sum directly? Only tells you:“Have I seen this running sum before?”
# That corresponds to subarrays with sum 0, not k.

# Why NOT check k directly?
# “Did some prefix sum equal k?”
# That only finds subarrays starting at index 0.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashMap = {0 : 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hashMap:
                count += hashMap[prefix_sum-k]
            hashMap[prefix_sum] = hashMap.get(prefix_sum, 0)+1

        return count       