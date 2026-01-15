#limiting factors are width and min(h1,h1), the min height. So we start with max width possible (two-pointer greedy approach) and the move the pointers accordingly to maximize the area possible.
#after we have explored the max water possible with a pointer (left or right), we move it.

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0

        left , right = 0, len(height)-1

        while left <= right: #it can be left < right also
            area = min(height[left], height[right]) * (right-left)

            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_area