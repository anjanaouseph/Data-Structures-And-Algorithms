# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #here we shud check along the path
        #using iteration stack

        stack = [(root,float('inf'),float('-inf'))]

        while stack:
            root, high, low = stack.pop()

            if not low < root.val < high:
                return False

            if root.left:
                stack.append((root.left, root.val, low))

            if root.right:
                stack.append((root.right, high, root.val))

        return True
       
    

# TC: O(N)
# SC: O(h), which is O(n) in worst case (skewed) and O(log n) in balanced tree