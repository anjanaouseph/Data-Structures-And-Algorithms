# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in a bst in-order traversal gives the nodes in ascending order

        if not root:
            return -1

        count = [1]

        ans = [-1]

        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if ans[0] != -1:
                return

            if count[0] == k:
                ans[0] = root.val #stop recursion if ans is found
                return

            count[0] += 1

            dfs(root.right)

        dfs(root)

        return ans[0]