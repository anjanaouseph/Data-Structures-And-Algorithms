class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #hashing based solution
        nums.sort()

        result = set()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:#to avoid duplicates iterate till u find next unique
                continue

            inner_sum = -nums[i]
            self.twoSum(nums, i, inner_sum, result )

        return [list(triplet) for triplet in result]

    def twoSum(self, nums, start, target, result):
        seen = set()
        for j in range(start+1, len(nums)):
            complement = target - nums[j]
            if complement in seen:
                triplet = sorted([complement, nums[j], nums[start]]) #O(3) 
                result.add(tuple(triplet))
            else:
                seen.add(nums[j])

# You only skip duplicates after a valid triplet
# You never skip a value that could form a new combination, so can't add duplicate check condition for inner j loop. Use sorting here.
# Order guarantees no missed cases

# Time Complexity: O(nlogn) + O(n2) + O(n) = O(n2)
# space complexity: O(n)