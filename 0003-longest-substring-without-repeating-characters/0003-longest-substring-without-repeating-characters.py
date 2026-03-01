class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashMap = {}

        slow = 0

        max_len = 0

        for i in range(len(s)):
            if s[i] in hashMap:
                slow = max(slow,hashMap[s[i]]+1)

            hashMap[s[i]] = i

            max_len = max(max_len, i-slow+1)

        return max_len
        
        