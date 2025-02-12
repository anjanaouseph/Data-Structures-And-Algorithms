class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #sliding window

        left , right = 0,0 
        max_len = 0
        num_zeroes = 0

        while right<len(nums):
            if nums[right] == 0: #add this condition here in the begining so that we are checking this as soon as we increment the right pointer.
                num_zeroes += 1

            while num_zeroes>k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len        