class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
        if n == 0:
            return []

        def backtrack(open, close):
            #base case
            if len(sol) == 2*n:
                res.append("".join(sol))
                return

            if open < n:
                sol.append('(')
                backtrack(open+1, close)
                sol.pop()

            if open > close:
                sol.append(')')
                backtrack(open, close+1)
                sol.pop()

        backtrack(0,0)
        return res