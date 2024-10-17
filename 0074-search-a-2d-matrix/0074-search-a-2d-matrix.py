class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROW, COL = len(matrix),len(matrix[0])
        top, bot = 0, ROW-1

        while top <= bot:
            row = (top+bot)//2 #to truncate the decimal and get only integer part
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not top<=bot: #this means the element is absent in the matrix
            return False

        l, r = 0, COL-1
 
       # row = (top+bot)//2  #to ensure you're performing the second binary search (within the row) using the final, most accurate top and bot values.

        while l<=r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid-1
            else:
                return True #we found the row and column containing the target
        
        return False
        