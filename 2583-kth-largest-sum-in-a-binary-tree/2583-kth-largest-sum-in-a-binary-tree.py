# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        #bfs

        largest_sum = [] #stores the sum across all levels
        sum = [0]

        queue = deque([root])

        while queue:
            sum[0] = 0
            for i in range(len(queue)):
                root = queue.popleft()

                sum[0] += root.val

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)

            largest_sum.append(sum[0])

        #now use heap which is min heap of size k
        if len(largest_sum) < k:
            return -1

        heap = []

        for num in largest_sum:
            heapq.heappush(heap,num)

            if len(heap)>k:
                heapq.heappop(heap)
        
        return heap[0]




        