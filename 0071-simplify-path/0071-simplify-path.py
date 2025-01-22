class Solution:
    def simplifyPath(self, path: str) -> str:
        #use stack to skip the current dir if we encounter a ..
        
        stack = []

        path_stack = path.split("/")#splits the string at each / and returns a list of substrings.  #O(n)

        for item in path_stack:#o(n)
            if item == "." or item == "":
                continue #skip '.' and empty string skip them
            elif item == "..":
                if stack:
                    stack.pop() #because it means we go to back to the parent directory, so remove the current director which is the element on top of the stack
            else:
                stack.append(item)

        return "/"+"/".join(stack)#o(n)

        

        