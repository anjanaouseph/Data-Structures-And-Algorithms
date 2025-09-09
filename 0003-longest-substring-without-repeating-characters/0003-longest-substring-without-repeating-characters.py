class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        left = 0
        right = 0
        max_length = 0
        i,j = 0,0

        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            if right-left+1 > max_length:
                max_length = right-left+1
                i = left
                j = right

            right = right+1

        print(s[i:j+1])
        return max_length     