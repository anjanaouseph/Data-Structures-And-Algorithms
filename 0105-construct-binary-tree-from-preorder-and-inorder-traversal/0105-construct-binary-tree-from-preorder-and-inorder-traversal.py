# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #create a hashmap for inorder for lookup
        hashMap = {val : index for index,val in enumerate(inorder)}

        def construct(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            rootval = preorder[pre_start]

            root = TreeNode(rootval)

            mid = hashMap[rootval] #use hashmap for O(1) lookup instead of index()

            left_elements = mid - in_start

            root.left = construct(pre_start+1, pre_start+left_elements, in_start, mid-1 )#instead of array slicing we pass the pointers

            root.right = construct(pre_start+left_elements+1, pre_end, mid+1, in_end)

            return root

            

        return construct(0, len(preorder)-1, 0, len(inorder)-1)#we pass the indices of elements in each list
        