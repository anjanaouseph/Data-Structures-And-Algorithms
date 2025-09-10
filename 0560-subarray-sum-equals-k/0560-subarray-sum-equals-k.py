class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        hashMap = collections.defaultdict(int)
        hashMap[0] = 1
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num

            if current_sum-k in hashMap:
                count += hashMap[current_sum-k]

            hashMap[current_sum] += 1

        return count         