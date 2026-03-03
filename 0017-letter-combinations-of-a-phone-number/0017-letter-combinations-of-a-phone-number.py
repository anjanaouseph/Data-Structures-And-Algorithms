class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""

        hashMap = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []
        sol = []

        n = len(digits)

        def backtrack(i):
            #base case
            if i == n:
                return ans.append("".join(sol))
            
            for ch in hashMap[digits[i]]:
                sol.append(ch)
                backtrack(i+1)
                sol.pop()

        backtrack(0)

        return ans
        