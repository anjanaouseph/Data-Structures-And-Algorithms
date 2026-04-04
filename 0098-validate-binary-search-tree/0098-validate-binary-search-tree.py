# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #here we shud check along the path
       
        def dfs(root, high, low):
            if not root:
                return True

            if not low < root.val < high:
                return False

            return dfs(root.left,root.val,low) and dfs(root.right,high,root.val)
            #think in terms of upper and lower limits at each node

        return dfs(root, float('INF'), float('-INF'))
        return True   

# TC: O(N)
# SC: O(h), which is O(n) in worst case (skewed) and O(log n) in balanced tree