# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #iterative solution in DFS
        if not root or not q or not p:
            return None

        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                if curr.right:
                    curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                if curr.left:
                    curr = curr.left
            else:
                return curr

        return None        