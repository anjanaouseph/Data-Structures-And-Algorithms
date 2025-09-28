class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return False
        #convert to lower case
        s_lower = s.lower()

        #remove all non-alpha numeric characters
        res = []

        for s in s_lower:
            if s.isalnum():
                res.append(s)

        "".join(res)

        left = 0
        right = len(res)-1

        while left < right:
            if res[left] != res[right]:
                return False
            
            left += 1
            right -=1

        return True    