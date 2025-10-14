class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_water = 0

        left = 0
        right = len(height)-1

        while left < right:
            area = min(height[left], height[right])*(right-left) #start at max width

            max_water = max(max_water, area)

            if height[left]<= height[right]:#we try to maximize the smaller constraint in the aim to find the bigger area
                left += 1
            else:
                right -= 1

        return max_water     