class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix), len(matrix[0])

        top, bot =0, row-1

        #do binary search to narrow down the row
        while top <= bot:
            mid1 = (top+bot)//2

            if target > matrix[mid1][-1]:
                top = mid1+1

            elif target < matrix[mid1][0]:
                bot = mid1-1
            else:
                break

        if top > bot:
            return False #element doesn't exist

        #we have identified the row above which will be top = bot
        #do binary search again on the row we identified

        left,right = 0,col-1

        while left <= right:
            mid = (left+right)//2

            if target > matrix[mid1][mid]:
                left = mid+1
            elif target < matrix[mid1][mid]:
                right = mid-1
            else:
                return True

        return False


        

        
        