class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True

        s_proper = re.sub(r'[^A-Za-z0-9]',"",s)

        i = 0
        j = len(s_proper)-1


        while i<j:
            if s_proper[i].lower() != s_proper[j].lower():
                return False

            i += 1
            j -= 1

        return True
