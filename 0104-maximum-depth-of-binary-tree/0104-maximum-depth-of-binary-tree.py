# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        #we need to do a BFS
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()
            level = max(level, depth)

            if node.left:
                queue.append((node.left,depth+1))

            if node.right:
                queue.append((node.right, depth+1))

        return level
            








        