class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        res = ""

        rows = [[] for i in range(numRows)] #no restrictions on columns

        i = 0

        for char in s: #below code makes sure i is from 0 to numRows--1        
            
            rows[i].append(char)

            if i == 0:#hits upper boundary
                d = 1 #go down

            elif i == numRows-1:#if it hits the bottom boundary then go up
                d = -1
            i += d

        for row in rows:
            res += "".join(row)

        return res

# Time Complexity: O(n)
# You iterate through the string s once → O(n)
# Then you iterate through all rows to build the result → total characters still add up to n
# So overall:
# O(n + numRows) You loop through the string → O(n)
# You loop through rows → O(numRows)
# You walk through the string once to distribute letters
# Then you collect them once from rows
# You never reprocess the entire string per row.

# Space Complexity: O(n + numRows) = O(n)
# You’re storing:
# All characters → n
# The rows structure → numRows