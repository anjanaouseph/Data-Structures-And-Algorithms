# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(root):#preorder
            if not root:
                res.append('N')
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        result = data.split(",")

        def reconstruct():
            if result[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(result[self.i]))
            self.i += 1
            node.left = reconstruct()
            node.right = reconstruct()

            return node

        return reconstruct()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# Preorder is preferred because it processes the root first, which aligns naturally with recursive tree construction. Inorder doesn’t uniquely define the tree, and postorder is harder since the root appears last. Level order works but requires additional data structures.
# To reconstruct a tree using one traversal, we need:
# Traversal that gives root position clearly
# PLUS null markers to preserve structure