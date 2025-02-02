# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_val = 0

        def dfs(root, pos):
            if not root:
                return (0,0)

            left, leftpos = dfs(root.left, pos+1)
            right, rightpos = dfs(root.right, pos+1)

            sum = left+right+root.val
            count = leftpos+rightpos+1

            average = sum/count #use float
            self.max_val = max(average, self.max_val)

            return (sum, count)
            
        dfs(root,0)
        return self.max_val