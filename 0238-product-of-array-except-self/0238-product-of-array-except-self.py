class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Solution with O(N) time and O(1) space complexity
        n = len(nums)
        res = [1]*n

        pdt_left = 1
        pdt_right = 1

        for i in range(n):
            res[i] = pdt_left
            pdt_left *= nums[i]

        for i in range(n-1, -1, -1):
            res[i] *= pdt_right
            pdt_right *= nums[i]

        return res       