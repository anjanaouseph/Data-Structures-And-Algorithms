# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #iterative solution for bst lca

        curr = root
        lca = root

        while curr:
            lca = curr
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left

            else:
                return curr

        return None     