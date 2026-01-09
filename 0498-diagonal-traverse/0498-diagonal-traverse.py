class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        m = len(mat) #rows
        n = len(mat[0]) #cols

        row = 0
        col = 0
        dir = True

        #find all cases where we need to reverse directions

        while row < m and col < n:
            result.append(mat[row][col]) #always add the first element

            if dir: #for upward traversals boundaries are roof and  right so when we hit boundaries
                if row == 0 and col != n-1: #roof boundary is reached as roof boundary is row = zero
                    col += 1
                    dir = False
                elif col == n-1: #right boundary is reached as right boundary = col n-1 and the corner case is also reached
                    row += 1
                    dir = False
                else:
                    row -= 1 #general cases in upward dir when we are not hitting boundaries
                    col += 1

            else: #for downward traversal left and bottom are boundaries
                if row == m-1: #hit bottom boundary and corner case is handled here
                    col += 1
                    dir = True

                elif col == 0 and row != m-1: #hit left boundary or the corner case
                    row += 1
                    dir = True
                else:
                    #generally
                    col -= 1
                    row += 1
        return result

#we need to handle the intersection of two boundaries or the corner cases here as it can also go OOB

        

# up-right diagonals don’t always end by hitting the top wall.
# Sometimes they end by hitting the right wall (j == n). In that case, resetting i = 0 is wrong.
# Down-left diagonals sometimes end at the left wall (j == -1) and sometimes at the bottom wall (i == m), and each needs a different fix.

#when to decide i have to flip the directions
#in which direction we have to flip
#if we are on (0,0) how to decide which index to go to.