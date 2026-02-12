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

        #BFS
        queue = deque([root])

        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)       
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result   

# Time Complexity: O(N)
# Space Complexity : O(w) which is O(1) for skewed trees and O(N/2) for complete trees     