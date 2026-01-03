# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root, p, q):
            if not root:
                return None
            lca[0] = root
            if p.val > root.val and q.val > root.val:
                search(root.right,p, q)
            elif p.val < root.val and q.val < root.val:
                search(root.left,p, q)
            else:
                return #case where both branches diverge and where p == root or q == root

        search(root,p,q)
        return lca[0]
                
            