# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]
        ans = [0]

        #in-order traversal using DFS 

        def in_order(node):
            if not node:
                return 
            
            in_order(node.left)
            
            if count[0] == 1:
                ans[0] = node.val

            count[0] -= 1

            if count[0]>0:
                in_order(node.right)

        in_order(root)
        return ans[0]


            


        