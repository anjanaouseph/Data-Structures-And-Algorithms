class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2 pointer based solution
        nums.sort()

        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break #early stopping as we are already sorted the array in asc order so elements after this will always be larger and
                #we won't get sum = 0.
            
            left = i+1
            right = len(nums)-1
            inner_sum = -nums[i]

            while left < right:
                if nums[left]+nums[right] == inner_sum:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right and nums[left] == nums[left-1]):
                        left += 1

                    while (left<right and nums[right] == nums[right+1]):
                        right -= 1

                elif nums[left]+nums[right] > inner_sum:
                    right -=1
                    while (left<right and nums[right] == nums[right+1]):
                        right -= 1

                else:
                    left += 1
                    while (left < right and nums[left] == nums[left-1]):
                        left += 1
                

                #to handle inner duplicacy. we can also check if array is going OOB
                #but best way to do is by checking the base condition again
                #if base condition variables have been mutated.

        return result


# You only skip duplicates after a valid triplet if found
# Time Complexity: O(nlogn) + O(n2) = O(n2)
# space complexity: O(1)