class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest = float('inf')
        closest_sum = nums[0]+nums[1]+nums[2]

        #without skipping duplicates
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1

            while left < right:
                sum = nums[i]+nums[left]+nums[right]

                absolute = abs(target-sum) #measures the closeness

                if absolute<closest:
                    closest = min(closest, absolute)
                    closest_sum = sum

                if sum >= target:
                    right -= 1

                if sum < target:
                    left += 1

        return closest_sum


# TC: O(nlogn)+O(n*n)
# SC: O(1)