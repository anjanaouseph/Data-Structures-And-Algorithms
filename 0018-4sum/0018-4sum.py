class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sorting and then using 2 loops and 2 pointers
        #return an array of all the unique quadruplets -> no duplicates allowed
        nums.sort()

        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = len(nums)-1

                inner_sum = target-(nums[i]+nums[j])

                while left < right:
                    sum = nums[left]+nums[right]
                    if  sum == inner_sum:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1

                        while (left < right and nums[left] == nums[left-1]):
                            left += 1

                        while (left<right and nums[right] == nums[right+1]):
                            right -= 1

                    elif sum > inner_sum:
                        right -= 1
                        while (left<right and nums[right] == nums[right+1]):
                            right -= 1

                    else:
                        left += 1
                        while (left<right and nums[left] == nums[left-1]):
                            left += 1

        return result       

# TC: O(nlogn)+O(n*n*n) = O(n3)
# SC: O(1)
# NOTE: here don't check if nums[i] > target, then break. similarly don't check if nums[j]>target, break
# because here since target can be negative, this can be offseted.
# In 3 sum pbm target is 0 always, not random, so if first no after sorting is positive, then it won't be offseted by later no.s.
# so in 3 sum with target not 0, code is same but without that early stopping condition