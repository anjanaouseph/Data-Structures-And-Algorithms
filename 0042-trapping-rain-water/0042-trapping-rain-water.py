class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = 0
        max_right = 0

        left_max = [0]*len(height)
        right_max = [0]*len(height)

        for i in range(len(height)):
            j = -i-1 #to start index from the back
            left_max[i] = max_left
            right_max[j] = max_right

            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])


        summ = 0

        for i in range(len(height)):
            potential = min(left_max[i], right_max[i])

            summ += max(0,potential - height[i])


        return summ