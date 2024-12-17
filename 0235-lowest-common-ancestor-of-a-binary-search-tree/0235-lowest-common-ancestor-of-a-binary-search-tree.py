# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [0] #global variable is a mutable list object

        def height(root):
            if not root:
                return

            lca[0] = root

            if p.val > root.val and q.val> root.val:#search the right side as values are greater than root
                height(root.right)
            elif p.val < root.val and q.val<root.val:#search left side
                height(root.left)
            else: #split happens one value is larger and one value is smaller than root or root is equal to one of the values then also return current root as LCA
                return

        height(root)

        return lca[0]