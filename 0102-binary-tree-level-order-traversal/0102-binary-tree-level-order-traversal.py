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

        queue = deque([root])

        levels = []

        while queue:
            res = [] #The temporary list for each level can also take up to O(n) space in the worst case, but it does not accumulate across iterations. Same space taken as queue.
            for i in range(len(queue)):
                node = queue.popleft()

                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(res)

        return levels     

# Time Complexity: O(N)
# Space Complexity : O(W) which is O(1) for skewed trees and O(N/2) for complete trees  