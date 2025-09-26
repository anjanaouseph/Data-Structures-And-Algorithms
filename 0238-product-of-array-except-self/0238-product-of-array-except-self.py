class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pdt_left = 1
        pdt_right = 1
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(n):
            j = -i-1 #to store values from reverse

            prefix[i] = pdt_left
            suffix[j] = pdt_right

            pdt_left *= nums[i]
            pdt_right *= nums[j]

        return [ p*s  for p,s in zip(prefix, suffix)]