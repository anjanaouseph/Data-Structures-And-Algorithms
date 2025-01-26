class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []

        stack = []

        for i,height in enumerate(heights):
            while stack and height>=stack[-1][0]:
                    stack.pop()
            stack.append([height, i])

        res = []

        while stack:
            val, index = stack.pop()
            res.append(index)

        res.reverse() #The reason res.reverse() returns None is because the reverse() method in Python is designed to modify the list in place and not return a new list. This design follows the principle of command-query separation (CQS), which states that a method should either:Perform an action (like modifying an object) but not return a value.Return a value but not modify the object.
        return res
        