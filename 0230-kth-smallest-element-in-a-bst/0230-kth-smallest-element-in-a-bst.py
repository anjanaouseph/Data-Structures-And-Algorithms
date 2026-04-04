# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #max heap will be O(NlogK)

        #since its a BSR, in-order traversal will give the elements in sorted order.

        if not root or k <= 0:
            return -1

        def inorder(root):

            nonlocal k

            if not root:
                return

            left = inorder(root.left)

            if left is not None:
                return left
            #process current node
            k -= 1
            if k == 0:
                return root.val
            
            right = inorder(root.right)

            if right is not None:
                return right

        return inorder(root)  

# TC: O(N)
# SC: O(H) h = n for skewed tree and logN for balanced BST   