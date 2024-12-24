# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)


        dfs(root)
        return ",".join(res) # takes each element in the list res and combines them into a single string, separated by commas.eg: "1,2,N,N,3,N,N"     

    def deserialize(self, data):
        values = data.split(",")#The split() method in Python is used to break a string into a list of substrings based on a specified delimiter.The string is split at each comma, and the substrings are stored as list elements.
        i = 0

        def dfs():
            nonlocal i
            if values[i] == 'N':
                i += 1
                return None
            
            node = TreeNode(values[i])
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))