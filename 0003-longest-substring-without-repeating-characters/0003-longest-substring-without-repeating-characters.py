class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashMap = {}
        max_len = 0
        slow = 0 #marks the start of the current valid substring

        for i in range(len(s)):
            c = s[i]
            if c in hashMap:
                slow = max(slow, hashMap[c]+1) #For each character, we check if we’ve seen it before.
# If we have, we move the slow pointer to one position after the previous occurrence of that character, but only if that occurrence is inside the current substring.
# The max ensures we never move the slow pointer backward, which would break the window.

            hashMap[c] = i

            max_len = max(max_len, i-slow+1)

        return max_len

# Time Complexity : O(N)
# Space Complexity: O(1)

# If the duplicate character was seen inside the current window, we move slow past its previous index.
# If it was seen before the current window, we do nothing and keep slow where it is.
# This prevents slow from ever moving backward.
        