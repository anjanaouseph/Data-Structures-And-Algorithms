class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        array_set = set(nums)

        longest = 0

        for num in array_set:
            if num-1 in array_set:
                continue

            count = 1

            while num+1 in array_set:
                count += 1
                num = num+1
            
            longest = max(longest, count)

        return longest