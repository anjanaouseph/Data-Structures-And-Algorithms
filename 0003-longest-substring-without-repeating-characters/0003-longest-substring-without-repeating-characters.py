class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        visited = set()

        left = 0
        right = 0

        max_len = 0

        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])

            max_len = max(max_len, right-left+1)

            right += 1

        return max_len