class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in map:
                stack.append(c) #opening brackets append to stack
                continue
            if not stack or stack[-1] != map[c]:
                return False
            stack.pop()
        return not stack


        