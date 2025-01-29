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

        res = []

        hashMap = collections.defaultdict(list)

        queue = deque([[root,1]])

        while queue:
            length = len(queue)
            for i in range(length):
                node, column = queue.popleft()
                if node:
                    hashMap[column].append(node.val)
                if node.left:
                    queue.append([node.left, column-1])
                if node.right:
                    queue.append([node.right, column+1])

        for key in sorted(hashMap.keys()):
            res.append(hashMap[key])

        return res

        