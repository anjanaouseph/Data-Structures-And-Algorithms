# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #find height using DFS
        #diameter = left_height + right_height
        largest_diameter = [0]

        def height(root):#The height function is a nested function inside diameterOfBinaryTree, so it does not belong to the Solution class. Adding self as a parameter is unnecessary and will result in an error when calling it.
                if not root:
                    return 0

                left = height(root.left)
                right = height(root.right)
                diameter = left + right
                largest_diameter[0] = max(largest_diameter[0], diameter)
                #

                return max(left,right)+1

        height(root)
        return largest_diameter[0]

       


        