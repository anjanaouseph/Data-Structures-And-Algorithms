class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #brute force O(n2)
        #sorting + linear search
        nums.sort()
        result = []
        i = 0

        for expected in range(1, len(nums)+1):
            if i == len(nums) or nums[i] > expected:
                result.append(expected)
            while i < len(nums) and nums[i] == expected:
                i += 1

        return result        