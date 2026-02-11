class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        sett = set()

        left, right = 0, 0

        max_len = 0

        while right < len(s):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            sett.add(s[right])

            length = right-left+1

            max_len = max(max_len, length)

            right += 1
        return max_len      