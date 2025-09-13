class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        left = 0
        right = 0

        seen = set()
        length = 0

        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            length = max(length, right-left+1)
            right += 1

        return length