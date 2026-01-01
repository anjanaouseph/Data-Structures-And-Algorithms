class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])

        #now we will flatten 2D matrix to imaginary 1D Array. 
        #but we will map the values in 1D array to corresponding pos in 2D matrix
        #Treat the 2D matrix as a 1D sorted array using index mapping (mid / n, mid % n).
        low = 0
        total = row*col
        high = total-1

        while low <= high:
            mid = low + (high - low)//2

            if matrix[mid//col][mid%col] == target:
                return True
            elif target < matrix[mid//col][mid%col]:
                high = mid-1
            else:
                low = mid+1

        return False
        
    # Time Complexity = O(log(m*n)) #since we are doing BS on the flattened 1D array which has m*n elements
    # Space Complexity: O(1)