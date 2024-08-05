class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c=='+':
                stack.append(stack.pop() + stack.pop())
            elif c=='-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a) #in substraction order matters
            elif c=='*':
                stack.append(stack.pop() * stack.pop())
            elif c=='/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a)) #division order matters, also in py by
                #default its decimal division. So convert it to integer.
            else:
                stack.append(int(c)) #append all the characters. When encountering a symbol,pop the
                #prev characters in the stack and perform the operation
        return stack[0] #the only remaining value in stack will be the output of the expression.

