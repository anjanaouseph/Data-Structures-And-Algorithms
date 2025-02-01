# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = [0]

        def dfs(root, pos):
            if not root:
                return (0,0)

            left, leftpos = dfs(root.left, pos+1)
            right, rightpos = dfs(root.right, pos+1)

            sum = left+right+root.val #sum of the subtree
            pos = leftpos+rightpos+1 #no of nodes in the subtree

            if sum // pos == root.val: #check if root node's val is equal to avg of the subtree
                count[0] += 1

            return (sum, pos)

        dfs(root, 1)
        return count[0]