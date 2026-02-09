# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]

        max_depth = 0

        while stack:
            node, count = stack.pop()

            max_depth = max(max_depth, count)

            if node.left:
                stack.append((node.left, count+1))
            if node.right:
                stack.append((node.right, count+1))

        return max_depth        