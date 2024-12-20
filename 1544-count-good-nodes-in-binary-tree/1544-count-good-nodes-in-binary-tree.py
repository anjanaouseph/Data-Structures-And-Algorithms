# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #using recurrsion
        def find_nodes(node, value):
            if not node:
                return 0

            count = 0

            if node.val >= value:
                value = max(node.val, value)
                count = 1

            count += find_nodes(node.left, value)
            count += find_nodes(node.right, value)

            return count

        return find_nodes(root, root.val)

            

        