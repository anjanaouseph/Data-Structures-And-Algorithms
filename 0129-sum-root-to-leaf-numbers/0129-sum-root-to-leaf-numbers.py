# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = [0]

        if not root:
            return 0

        def dfs(root, sum):
            
            sum = sum*10 + root.val

            if not root.left and not root.right: #if leaf node, add to result
                result[0] += sum
                return
            if root.left:
                dfs(root.left, sum)
            if root.right:
                dfs(root.right, sum)             

        dfs(root, 0)
        return result[0]