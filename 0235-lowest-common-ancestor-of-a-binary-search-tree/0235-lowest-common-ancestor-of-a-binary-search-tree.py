# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):
            if not root:
                return

            lca[0] = root
            if root is p or root is q: #case where either p or q is root
                return
            elif root.val > p.val and root.val > q.val: #case where both are on left subtree
                search(root.left)
            elif root.val < p.val and root.val < q.val: #case where both are on right subtree
                search(root.right)
            else:
                return #case where they both are on either side of the root, so LCA will be the root

        search(root)
        return lca[0]