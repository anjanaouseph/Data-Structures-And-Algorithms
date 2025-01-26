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

        res.reverse()
        return res
        