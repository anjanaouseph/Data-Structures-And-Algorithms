# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        self.hashMap = { val : i for i,val in enumerate(inorder)}

        self.index = 0

        def buildSubTree (preorder, start, end): #start and end of inorder list
            if start > end:
                return None

            root_val = preorder[self.index]
            self.index += 1

            inorder_index = self.hashMap[root_val]

            root = TreeNode(root_val)

            root.left = buildSubTree(preorder, start, inorder_index-1)
            root.right = buildSubTree(preorder, inorder_index+1, end)

            return root

        return  buildSubTree(preorder, 0, len(inorder)-1)





        