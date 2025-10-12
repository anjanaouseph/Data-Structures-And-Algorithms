class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #to prevent duplicates, so we can check if i+1 and i are same element or not

        res = []

        for i,a in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                three_sum = a+nums[left]+nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])

                    left += 1 #increment that left pointer to avoid duplicates of left,right
                    while nums[left] == nums[left-1] and left<right: #just need to increment the left to avoid duplicates, the 2 pointer alg will take care of right pointer
                        left += 1

        return res