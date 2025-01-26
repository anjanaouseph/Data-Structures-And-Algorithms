class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #solution without stack

        max_height = 0

        res = []

        for i in range(len(heights)-1,-1,-1):
            if heights[i] > max_height:
                max_height = heights[i]
                res.append(i)

        res.reverse()

        return res
        