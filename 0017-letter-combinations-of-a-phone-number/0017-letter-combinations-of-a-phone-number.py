class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashMap = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = [] #O(4^n * n)
        sol = [] #O(n) per recursion stack

        n = len(digits)

        def backtrack(i):
            #base case
            if i == n:
                return ans.append("".join(sol))#O(n)
            
            for ch in hashMap[digits[i]]:
                sol.append(ch)
                backtrack(i+1) #Only one recursive path exists at a time.
                sol.pop()

        backtrack(0)

        return ans
        

# Explanation:

# Each digit maps to multiple characters.
# So this is a combinatorial problem where we need to generate all possible letter combinations.
# Since we need to explore all possibilities, this is naturally a backtracking problem.
# At each position, we have multiple choices.
# For example, if the digit is '2', we can choose 'a', 'b', or 'c'.
# So for each digit, I try every possible character, move to the next digit, and continue building the string.

# “When the index reaches the length of the digits string, it means I’ve constructed one valid combination.
# So I join the characters and add it to the result.”

# “At index i, I look up all possible letters mapped to digits[i].
# For each letter:
# I add it to the current combination
# Recursively move to the next digit
# Then backtrack by removing the letter”

# Time Complexity:
# There are at most 4^n combinations since each digit has up to 4 letters.
# For each combination, we build a string of length n.
# Therefore, time complexity is O(4^n * n).

# Space Complexity:
# Auxiliary space is O(n) due to recursion depth and the temporary list.
# Output space is O(4^n * n) because we store all combinations.