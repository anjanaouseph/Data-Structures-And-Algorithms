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

        #create a hashmap to store keys as columns and values are list of nodes at a column
        hashMap = defaultdict(list)
        min_col = max_col = 0

        queue = deque([(root, 0)])#add root and its current column which is 0

        while queue:
            length = len(queue)
            for i in range(length):
                node, column = queue.popleft()

                if node:
                    #to find the min and max column values possible
                    hashMap[column].append(node.val)
                    queue.append((node.left, column-1))
                    queue.append((node.right, column+1))

                    min_col = min(min_col, column)
                    max_col = max(max_col, column)

        return [hashMap[column] for column in range(min_col, max_col+1)]