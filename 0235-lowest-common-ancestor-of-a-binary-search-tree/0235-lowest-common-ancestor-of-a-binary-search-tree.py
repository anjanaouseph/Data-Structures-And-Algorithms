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

        stack = [root]

        while stack:
            size = len(stack)
            for i in range(size):
                root = stack.pop()

                if root.val == p.val or root.val == q.val:
                    return root
                elif p.val > root.val and q.val > root.val:
                    if root.right:
                        stack.append(root.right)
                elif p.val < root.val and q.val < root.val:
                    if root.left:
                        stack.append(root.left)
                else:
                    return root

        return None






        