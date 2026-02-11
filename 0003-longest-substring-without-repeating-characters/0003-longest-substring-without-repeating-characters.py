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
                #check if duplicate is part of current substring or before it
                if hashMap[c] >= slow:#this means part of current substring so move slow ptr
                    slow = hashMap[c]+1
                else:
                    slow = slow #duplicate char is behind current substring so skip, keep slow as it is
                    
                #if slow ptr has gone past the index of c, then take the current pos of slow ptr, meaning the duplicate is not part of current substring, else jump slow to index+1

            hashMap[c] = i

            max_len = max(max_len, i-slow+1)

        return max_len

# Time Complexity : O(N)
# Space Complexity: O(1)

# If the duplicate character was seen inside the current window, we move slow past its previous index.
# If it was seen before the current window, we do nothing and keep slow where it is.
# This prevents slow from ever moving backward.
        