# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_val(node,min,max):
            if not node:#if we reach the end of the tree return Tre
                return True

            if node.val <= min or node.val >= max:
                return False

            return is_val(node.left, min, node.val) and is_val(node.right, node.val, max)
        #when u go left update the maximum and when u go right update the minimum to the previous node's values

        return is_val(root, float('-inf'), float('inf'))



        