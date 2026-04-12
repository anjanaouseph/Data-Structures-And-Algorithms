class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest = float('inf')
        closest_sum = 0

        #it says unique soln exists, there can be duplicates but i am skipping duplicates for better optimization
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:#t skips duplicate values for the first element of the triplet
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[left]+nums[right]+nums[i]

                abs_diff = abs(target-sum) #this measure the closeness

                if abs_diff < closest:
                    closest = min(closest, abs_diff)#stores smallest closesness so far
                    closest_sum = sum

                if sum >= target:#minimize the sum
                    right -= 1

                    while (left < right and nums[right] == nums[right+1]): #skipping duplicates here
                        right -= 1

                if sum < target:
                    left += 1

                    while (left<right and nums[left] == nums[left-1]):#skipping duplicates
                        left += 1

        return closest_sum  

# TC: O(nlogn)+O(n*n)
# SC: O(1)