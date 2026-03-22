# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #if nulls are present we can construct tree from a single traversal like how LC does.
        #if no nulls present then we need two traversals. null tells you where children are missing.
        # We need two traversals. (e.g., preorder + inorder) unless additional constraints like BST  properties are given.
        #inorder is needed because it tells the left vs right split.

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root_index = inorder.index(root_val) #O(N)

        #slice the arrays
        in_left = inorder[:root_index] #O(K)
        in_right = inorder[root_index+1:] #O(K-1)
        pre_left = preorder[1:len(in_left)+1]
        pre_right = preorder[len(in_left)+1:]

        #k+(n−k)+k+(n−k)≈2n
        #per recrusion cal it becomes n,n-1,n-2 so its O(N^2)
        #recursion space complexity is O(N)
        #Space complexity: O(n^2) due to list slicing.

        root = TreeNode(root_val)

        root.left = self.buildTree(pre_left,in_left)
        root.right = self.buildTree(pre_right,in_right)

        return root        

# TC: O(n^2)
# SC: O(n^2)