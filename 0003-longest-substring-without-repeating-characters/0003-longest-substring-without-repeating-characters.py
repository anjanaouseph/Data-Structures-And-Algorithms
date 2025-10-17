class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not len(s):
            return 0

        sett = set()

        left = 0
        right = 0
        max_length = 1

        while right < len(s):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sett.add(s[right])
            max_length = max(max_length, right-left+1)
            right += 1

        return max_length   