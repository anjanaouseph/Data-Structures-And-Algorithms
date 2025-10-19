class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0

        left = 0
        right = 0

        char_map = [0]*26 #to keep track of the count of characters in a particular window.

        while right < len(s):

            char_map[ord(s[right])-ord('A')] += 1

            while (right-left+1)-max(char_map)>k: #means the window is not satisfying
            #max(char_map) scans 26 entries; that’s O(26)=O(1).
                char_map[ord(s[left])-ord('A')] -= 1
                left += 1

            longest = max(longest, right-left+1)
            right += 1
        
        return longest