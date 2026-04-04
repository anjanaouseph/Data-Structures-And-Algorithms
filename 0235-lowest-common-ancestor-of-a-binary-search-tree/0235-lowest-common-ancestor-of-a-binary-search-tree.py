# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = [float('-inf')]
        
        def lowest_ancestor (root, p, q):

            if not root:
                return None

            lca[0] = root

            if root.val > p.val and root.val > q.val: #both are in left side
                return lowest_ancestor(root.left,p,q) #go to the left side
            if root.val < p.val and root.val < q.val:
                return lowest_ancestor(root.right,p, q)

            else:
                return lca[0]

        return lowest_ancestor(root,p,q)        

# TC: O(N)
# SC: O(H)