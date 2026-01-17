class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #hashing based solution
        nums.sort()

        result = set()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:#to avoid duplicates iterate till u find next unique
                continue

            inner_sum = -nums[i]
            seen = set()
            for j in range(i+1,len(nums)):
                compliment = inner_sum - nums[j]

                if compliment in seen:
                    triplet = sorted([compliment, nums[j], nums[i]])
                    result.add(tuple(triplet))
                seen.add(nums[j])

        return [list(triplet) for triplet in result]

# You only skip duplicates after a valid triplet
# You never skip a value that could form a new combination, so can't add duplicate check condition for inner j loop. Use sorting here.
# Order guarantees no missed cases