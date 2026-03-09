class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        #check for whitespace
        i = 0

        while i<len(s) and s[i] == " ":
                i += 1 

        if not s:
            return 0 #case when string only has white space

        sign = 1      

        if i<len(s) and s[i] == '+':
            sign = 1
            i += 1
        elif i<len(s) and s[i] == '-':
            sign = -1
            i += 1

        parsed = 0

        while i < len(s):
            curr = s[i]

            if not s[i].isdigit():
                break

            parsed = (parsed*10)+int(curr)
            i += 1

        parsed *= sign

        if parsed > 2**31-1:
            return 2**31-1
        elif parsed <= -2**31:
            return -2**31
        else:
            return parsed
              