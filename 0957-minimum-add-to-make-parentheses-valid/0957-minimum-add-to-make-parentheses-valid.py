class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
    
        left = 0
        right = 0
        count = 0

        for char in s:
            if char == '(':
                left += 1
            elif char == ')' and left > right:#only close if there is an open parenthesis
                right += 1
            else:
                count += 1 #the extra ')' which doesnt have a '(' to close comes here
        count += (left- right) #add addition open '(' parenthesis as well.

        return count