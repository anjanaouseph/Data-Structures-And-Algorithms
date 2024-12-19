# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #using DFS

        if not root:
            return 0

        value = root.val
        count = 0
        
        stack = [[root, value]]

        while stack:
            node, value = stack.pop()
            if node:
                if node.val >= value:
                    count += 1
                    value = max(node.val, value)
                stack.append([node.left, value])
                stack.append([node.right, value])


        return count

            


        


        