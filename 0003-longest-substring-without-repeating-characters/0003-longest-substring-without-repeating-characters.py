class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        map = {}

        while r < len(s):

            if s[r] in map and map[s[r]]>=l: #within the range
                l = map[s[r]]+1 #jump l to the position after r to get bigger or same size substring
           
            max_len = max(max_len, r-l+1)

            map[s[r]] = r

            r += 1

        return max_len        