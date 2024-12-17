# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #iteration

        lca = root

        while lca:
            if lca.val < p.val and lca.val < q.val:
                lca = lca.right
            elif lca.val > p.val and lca.val > q.val:
                lca = lca.left
            else:
                return lca

