# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float('-inf')] #initialize to ) because Ensures that negative path sums are considered valid.

        def calculateSum(root):#why return type not need? ->int
            if not root:
                return 0

            left_sum =  max(0,calculateSum(root.left))
            right_sum =  max(0,calculateSum(root.right))

            max_sum[0] = max(max_sum[0], root.val+left_sum+right_sum)

            return max(root.val+left_sum, root.val+right_sum)

        calculateSum(root)
        return max_sum[0]
            