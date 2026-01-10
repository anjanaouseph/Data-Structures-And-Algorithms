class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #top bottom left and right defines the boundaries and after each spiral, these boundaries
        #changes

        m = len(matrix) #rows
        n = len(matrix[0]) #cols
        result = []

        top, left, right, bottom = 0, 0, n - 1, m - 1

        while top <= bottom and left <= right:

            for i in range(left, right+1):
                result.append(matrix[top][i])

            top += 1

            for i in range(top, bottom+1): #if top > bottom then will this for loop won't run
                result.append(matrix[i][right])
            
            right -= 1

            if top <= bottom: #if base condition var gets mutated always check them again
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])

            bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
            left += 1

            
        return result    