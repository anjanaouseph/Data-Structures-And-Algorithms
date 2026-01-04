from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for i in range(len(nums)):
            if target-nums[i] in hashMap:
                return [hashMap[target-nums[i]], i]

            hashMap[nums[i]] = i

        return result