class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        #brute force involves looping over every substring and checking if it is a palindrome
        #palindrome can be even length and odd length, so the idea is to check for odd length and even length palindrome occurance at every index. eg bbbd bbdd

        res = [0,0]
        longest = 0

        for i in range(len(s)):
            #first lets check for odd length palindroms for every index
            left, right = i,i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = max(longest, right-left+1)
                    res[0] = left
                    res[1] = right #creates new string O(K) time complexity
                left -= 1
                right += 1

            #check for even length palindroms
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = max(longest, right-left+1)
                    res[0] = left
                    res[1] = right
                left -= 1
                right += 1

        return s[res[0] : res[1]+1]