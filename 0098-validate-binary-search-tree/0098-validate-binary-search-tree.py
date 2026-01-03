# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = collections.deque([(root, float("inf"), float("-inf"))])

        while queue:
            size = len(queue)
            for i in range(size):
                node, max_val, min_val = queue.popleft()
                if not min_val < node.val < max_val:
                    return False
                if node.left:
                    queue.append((node.left, node.val, min_val))
                if node.right:
                    queue.append((node.right, max_val, node.val))
        return True        