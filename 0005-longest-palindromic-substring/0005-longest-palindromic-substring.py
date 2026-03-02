class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        #palindrome can be even length and odd length, so the idea is to check for odd length and even length palindrome occurance at every index. eg bbbd bbdd

        longest = 0
        res = ""

        for i in range(len(s)):
            #first lets check for odd length palindroms for every index
            left, right = i,i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = max(longest, right-left+1)
                    res = s[left:right+1]
                left -= 1
                right += 1

            #check for even length palindroms
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = max(longest, right-left+1)
                    res = s[left:right+1]
                left -= 1
                right += 1

        return res