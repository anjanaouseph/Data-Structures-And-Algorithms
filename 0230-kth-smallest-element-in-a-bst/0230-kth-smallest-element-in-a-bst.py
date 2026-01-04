# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #iterative in-order traversal

        count = 1
        smallest = -1
        curr = root

        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()

            if count == k:
                smallest = node.val
                return smallest

            count = count+1

            curr = node.right

        return -1  