class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking

        res = []
        sol = []

        def backtrack(i):
            if i == len(nums):
                res.append(sol[:])
                return

            backtrack(i+1) #first u can backtrack without adding the nums[i]

            #then u backtrack adding the nums[i]

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop() #pop the added nums[i] from stack so that in the previous call stack sol[] can contain it's nums[i]

        backtrack(0)
        return res
        