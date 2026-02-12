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

        count = [0]

        #dfs
        def dfs(root, max_val):
            if not root:
                return

            if root.val >= max_val:
                count[0] += 1

            max_val = max(root.val, max_val)

            dfs(root.left, max_val)
            dfs(root.right, max_val)
        
        dfs(root,root.val)

        return count[0]      

# Time Complexity: O(N)
# Space Complexity: O(H) which is O(N) for skewed trees and O(logN) for balanced/complete trees 