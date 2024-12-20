# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #using recurrsion

        count = [0]

        def find_nodes(node, value):
            if not node:
                return count[0]

            if node.val >= value:
                value = max(node.val, value)
                count[0] += 1

            return find_nodes(node.left, value) and find_nodes(node.right,value)

        return find_nodes(root, root.val)

            

        