class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        curr_no = 0
        last_no = 0
        operation = '+'
        result = 0

        s= s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                curr_no = curr_no*10 + int(char)

            if not char.isdigit() or i == len(s)-1:
                if operation == '+':
                    result += last_no
                    last_no = curr_no

                elif operation == '-':
                    result += last_no
                    last_no = -curr_no

                elif operation == '*':
                    last_no *= curr_no
                    
                elif operation == '/':
                    last_no = int(last_no/curr_no)
                         
                operation = char
                curr_no = 0

        return result+last_no