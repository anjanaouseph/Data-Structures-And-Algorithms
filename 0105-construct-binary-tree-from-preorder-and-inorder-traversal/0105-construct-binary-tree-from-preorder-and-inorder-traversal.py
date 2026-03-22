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

        self.index = 0

        hashMap = {val : i for i, val in enumerate(inorder)}

        def buildSubtree(preorder, start, end):#these are in-order's start and end indices

            if start > end:
                return None

            root_val = preorder[self.index]
            root_index = hashMap[root_val] #O(1)
            self.index += 1 #preorder already gives nodes in the exact order we need to build the tree. prorder traversal is root → left subtree → right subtree. Recursion is also root→ build left→ build right

            root = TreeNode(root_val)

            root.left = buildSubtree(preorder, start, root_index-1 )
            root.right = buildSubtree(preorder, root_index+1, end)

            return root     

        return buildSubtree(preorder,0, len(inorder)-1)   

# TC: O(n)
# SC: O(n)

# In preorder: root,| then all left subtree nodes,| then all right subtree nodes

# So for any subtree:

# [root][left subtree of size L][right subtree]

# If the root is at preorder_start, then:
# left subtree starts at preorder_start + 1
# right subtree starts after skipping root and the whole left subtree: preorder_start + 1 + L