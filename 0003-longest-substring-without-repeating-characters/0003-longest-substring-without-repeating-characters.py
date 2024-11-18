class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        map = {}

        while r < len(s):

            map[s[r]] = map.get(s[r],0)+1

            while map[s[r]] > 1:#this means character repeating
            #Before checking if map[s[r]] > 1, you should ensure that s[r] exists in the map. If s[r] is not in the map, it will raise a KeyError. Here since iam adding to map no need to check if it exists
                map[s[l]] -= 1 #reduce freq by one for the character at 'l' which we are shrinking
                l += 1 #shrink the window
           
            max_len = max(max_len, r-l+1)

            r += 1

        return max_len        