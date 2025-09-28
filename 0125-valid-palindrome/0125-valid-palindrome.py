class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return False
        #convert to lower case
        s_lower = s.lower() #o(n) time and space

        #remove all non-alpha numeric characters
        res = [] #space is O(n)

        for s in s_lower: #O(n)
            if s.isalnum():
                res.append(s)

        left = 0
        right = len(res)-1

        while left < right: #O(n) time
            if res[left] != res[right]:
                return False
            
            left += 1
            right -=1

        return True    