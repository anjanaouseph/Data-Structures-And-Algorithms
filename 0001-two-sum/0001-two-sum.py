class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return []

        map = {}
         
        for i,num in enumerate(nums):
            if target - num in map:
                return [i, map.get(target - num)]
            else:
                map[num] = i

        return []