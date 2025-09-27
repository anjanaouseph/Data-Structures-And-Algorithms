class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        array_set = set(nums)

        longest = 0

        for var in array_set:
            if var-1 in array_set:
                continue

            count = 1

            while var+1 in array_set:
                count += 1
                var = var+1
            
            longest = max(longest, count)

        return longest