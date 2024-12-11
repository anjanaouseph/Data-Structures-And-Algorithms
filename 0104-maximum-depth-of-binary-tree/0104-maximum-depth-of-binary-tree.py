# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #DFS using stack

        queue = deque([(root,1)])

        level = 0

        while queue:
           node, depth = queue.popleft()
           level = max(level, depth)

           if node.left:
            queue.append((node.left, 1+depth))

           if node.right:
            queue.append((node.right, 1+depth))


        return level