class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashMap = {}
        max_len = 0
        slow = 0

        for i in range(len(s)):
            c = s[i]
            if c in hashMap:
                slow = max(slow, hashMap[c]+1)

            hashMap[c] = i

            max_len = max(max_len, i-slow+1)

        return max_len


        