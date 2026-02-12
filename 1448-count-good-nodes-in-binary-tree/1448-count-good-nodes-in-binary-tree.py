# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        #dfs
        stack = [(root, root.val)]

        count = 0

        while stack:
            node, max_val = stack.pop()

            if node.val >= max_val:
                count += 1

            if node.left:
                stack.append((node.left, max(node.left.val, max_val)))
            if node.right:
                stack.append((node.right, max(node.right.val, max_val)))

        return count       

# Time Complexity: O(N)
# Space Complexity: O(H) which is O(N) for skewed trees and O(logN) for complete trees 