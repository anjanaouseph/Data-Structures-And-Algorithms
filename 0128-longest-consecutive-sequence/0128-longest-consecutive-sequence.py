class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        sett = set(nums)

# For SETs: Time: O(n) average
# Space: O(n) worst case (O(u) where u = number of unique elements)
        longest = 0

        for nums in sett:
            if nums-1 in sett:
                continue

            count = 1

            while nums+1 in sett:
                count += 1
                nums = nums+1

            longest = max(longest, count)

        return longest     