# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #max heap will be O(NlogK)

        #since its a BSR, in-order traversal will give the elements in sorted order.

        if not root or k <= 0:
            return -1

       #iteration

        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop() #pop last added root

            #now process that root, which will be the leaf root of Left sub tree
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        return -1

# TC: O(N)
# SC: O(H) h = n for skewed tree and logN for balanced BST   