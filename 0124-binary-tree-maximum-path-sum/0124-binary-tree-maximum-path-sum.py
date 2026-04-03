# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('-inf')

        sum = [float('-inf')]

        def dfs(root):
            if not root:
                return 0

            sum_left = max(0,dfs(root.left)) #-1. --- but will be 0 Take this path only if it helps, otherwise ignore it, negative won't help. Don't add negative no to maximize anything
            sum_right = max(0,dfs(root.right)) #-3 --- 0 but will be 0

            sum[0] = max(sum[0], root.val+sum_left+sum_right) #check for -4

            return root.val + max(sum_left, sum_right)#just return the maximum path to the parent node

        dfs(root)        
        return sum[0]
