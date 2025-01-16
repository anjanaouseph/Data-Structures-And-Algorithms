# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if not root:
                return None

            if root == p or root == q:#if root is p or q then thats the LCA
                return root

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right: #if left and right subtree returns something then it means the current node is the LCA
                return root

            return left or right #if either exists return either value or returns None

        return dfs(root,p,q)
            