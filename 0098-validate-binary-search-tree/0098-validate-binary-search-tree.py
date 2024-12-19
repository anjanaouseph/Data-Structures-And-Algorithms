# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        min = float('-inf')
        max = float('inf')

        stack = [[root,min,max]]

        while stack:
            node, min, max = stack.pop()
            if node:
                if node.val <= min or node.val >= max:
                    return False
                stack.append([node.left, min, node.val])
                stack.append([node.right, node.val, max])

        return True



        