# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_list = []#to store node values of each level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_list.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
            res.append(level_list)

        return res