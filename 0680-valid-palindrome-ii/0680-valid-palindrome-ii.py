import re 
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]','', s)

        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                return self.del_char(s, left+1, right) or self.del_char(s, left, right-1) #we can delete either the left or right pointer's char. If after deleting either satisfies the palindrome condition, we can say True else False
            left+=1
            right-=1

        return True

    def del_char(self,s, i, j):

        while i<j:
         if s[i] != s[j]:
            return False
         else:
            i += 1
            j -= 1

        return True