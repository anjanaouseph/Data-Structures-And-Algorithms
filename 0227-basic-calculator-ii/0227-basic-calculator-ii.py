class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        curr_no = 0
        operation = '+'
        stack = []

        s = s.replace(" ","") #replace all empty spaces

        for i,char in enumerate(s):
            if char.isdigit():
                curr_no = curr_no * 10 + int(char)

            if not char.isdigit() or i == len(s)-1:
                if operation == '+':
                    stack.append(curr_no)

                elif operation == '-':
                    stack.append(-curr_no)

                elif operation == '*':
                    stack[-1] = stack[-1] * curr_no

                else:
                    stack[-1] = int(stack[-1] / curr_no)

                operation = char
                curr_no = 0

        return sum(stack)





        