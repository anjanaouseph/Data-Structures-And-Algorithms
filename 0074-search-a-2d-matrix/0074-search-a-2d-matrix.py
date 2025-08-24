class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #rows
        cols = len(matrix[0]) #cols

        top = 0
        bot = rows-1

        #do binary search on the rows first
        while top<=bot:
            mid = top + (bot - top)//2

            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else: #means we identified the row
                break

        if top>bot:
            return False #element doesn't exist

        #do binary search on the cols
        #don't return early with return False
        left = 0
        right = cols-1

        row = mid
        while left<=right:
            mid = left + (right-left)//2

            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                left = mid+1
            else:
                right = mid-1
        
        return False