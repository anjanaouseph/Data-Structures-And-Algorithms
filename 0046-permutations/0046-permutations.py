class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        sol = []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()

        return ans