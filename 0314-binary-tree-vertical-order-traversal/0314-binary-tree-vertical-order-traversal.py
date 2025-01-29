# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        min_col = 0
        max_col = 0

        res = []

        hashMap = collections.defaultdict(list)

        queue = deque([[root,1]])

        while queue:
            length = len(queue)
            for i in range(length):
                node, column = queue.popleft()
                min_col = min(min_col, column)
                max_col = max(max_col, column)
                if node:
                    hashMap[column].append(node.val)
                if node.left:
                    queue.append([node.left, column-1])
                if node.right:
                    queue.append([node.right, column+1])

        for i in range(min_col,max_col+1):
            if hashMap[i]:
                res.append(hashMap[i])

        return res

        