class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        curr_no = 0
        operation = '+'
        stack = []

        s = s.replace(' ','')

        for i, char in enumerate(s):
            if char.isdigit():
                curr_no = curr_no * 10 + int(char) #appending each digit to form a number. '1','2','3' forms '123'

            if not char.isdigit() or i == len(s) - 1:#not digit and if last character
                if operation == '+':
                    stack.append(curr_no)
                if operation == '-':
                    stack.append(-curr_no)
                if operation == '*':
                    stack[-1] = stack[-1]*curr_no
                if operation == '/':
                    stack[-1] = int(stack[-1] / curr_no) #should round towards 0. // rounds towards -inf and not 0

                operation = char
                curr_no = 0

        return sum(stack)
                