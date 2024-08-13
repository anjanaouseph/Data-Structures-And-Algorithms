class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #if the second block is smaller than first one then we can't extend it's area to the right
                index,height = stack.pop() #this index will be the starting of its area count
                max_area = max(max_area, height*(i-index)) #area will be (current loop position - the start of area) * height
                start = index #the smaller block can extend left 
            stack.append((start, h))

            #find the area of the remaning smaller blocks
        for index,height in stack:
            max_area =  max(max_area, height*(len(heights)-index))

        return max_area