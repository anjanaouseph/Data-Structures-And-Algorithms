class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}

        prefix_sum = 0
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in hashMap:
                count += hashMap[prefix_sum-k]

            hashMap[prefix_sum] = hashMap.get(prefix_sum, 0)+1

        return count

# Why use subarray sum here?
# Brute force: The most straightforward approach would be to try all possible subarrays and compute their sums. O(n^3)
# Since the array can contain negative numbers, sliding window won’t work reliably.
# With negative numbers, expanding or shrinking the window doesn’t guarantee predictable sum changes.
# Since we’re dealing with continuous subarrays, prefix sum is a natural approach.

#  a,b,c,d,e,f,g,h,i,j,k
#  prefix[f] = 13
#  prefix[k] = 20
#  the subarray from g to k equals 7 which is k
#  so at every prefix_sum just compute if prefix_sum-k has occured before or not
#  to handle the edge case of subarray sum happening in the beginning of the array we need to add {0:1} in hashmap so that if prefix_sum-k=0, By initializing the hashmap with {0:1}, we correctly count that as one valid starting point.