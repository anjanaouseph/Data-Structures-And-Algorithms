# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not p and not q:
            return -1

        if not p or not q:
            return -1

        ancestor = [root]

        def lca(root, p ,q):
            if not root:
                return

            ancestor[0] = root

            if p.val > root.val and q.val > root.val:
                lca(root.right,p, q)

            elif p.val < root.val and q.val < root.val:
                lca(root.left, p, q)

            else:
                return 

        lca(root,p, q)
        return ancestor[0]