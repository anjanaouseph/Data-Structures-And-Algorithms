class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1. first we remove extra closing "(". If there is a "(" which doesnt preceed an ")", we don't add it to the []

        filtered = []
        count = 0

        for c in s:
            if c == '(':
                count += 1
                filtered.append(c)
            elif c == ')' and count>0:#only add ) that succeed (, which means count will be >0
                count -= 1
                filtered.append(c)
            elif c != ')': #to handle edge case (()))
                filtered.append(c)

        res = []

        #iterate over filtered list backwards to remove additional ')'
        for c in filtered[::-1]:
            if c == '(' and count>0:
                count -= 1
            else:
                res.append(c)

        return ''.join(res[::-1])