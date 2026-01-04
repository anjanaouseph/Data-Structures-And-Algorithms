# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #since this is a BST, in-order traversal gives the nodes in increasing order
        count = [1]
        smallest = [0]

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            #process the root
            if count[0] <= k:
                smallest[0] = root.val
                count[0] = count[0]+1

            dfs(root.right)
        
        dfs(root)
        return smallest[0]