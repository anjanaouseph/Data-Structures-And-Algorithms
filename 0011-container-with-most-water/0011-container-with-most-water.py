class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height)-1
        area = 0

        while i<j:
            area = max(area, (min(height[i],height[j])*(j-i)))

            if height[i] < height[j]:#move along the smaller line to maximise the potential of finding the "longest shorter" line. < and <= works
                i+=1
            elif height[i] > height[j]:
                j-=1
            elif height[i] == height[j]:
                i+=1
                j-=1


        return area
        