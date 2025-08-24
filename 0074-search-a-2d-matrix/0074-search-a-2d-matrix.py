class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) #rows
        cols = len(matrix[0]) #cols

        left = 0
        right = rows-1

        #do binary search on the rows first

        while left <= right:#while loop exits when left > right
            mid = left + (right-left)//2

            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] > target:
                right = mid-1

            else:
                left = mid+1

        #do binary search on the cols
        #don't return early with return False
        row_new = right

        left = 0
        right = cols-1

        while left <= right:            
            mid = left + (right - left)//2

            if matrix[row_new][mid] == target:
                return True
            elif matrix[row_new][mid] > target:
                right = mid-1
            else:
                left = mid+1

        return False