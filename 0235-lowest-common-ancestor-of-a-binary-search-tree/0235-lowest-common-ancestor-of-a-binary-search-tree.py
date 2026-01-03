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
            elif p.val == root.val or q.val == root.val:
                return
            else:
                return #case where both branches diverge

        search(root,p,q)
        return lca[0]
                
            