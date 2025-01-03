class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        sett = set()

        while r<len(s):
            while s[r] in sett:
                sett.remove(s[l])
                l = l+1

            sett.add(s[r])

            max_len = max(max_len, r-l+1)

            r = r+1

        return max_len

        