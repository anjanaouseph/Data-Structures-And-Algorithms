class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        left = 0
        right = 0

        res = []

        q = collections.deque()
        
        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:#pop the values that are lesser than what we are going to add
                q.pop()
            
            q.append(right)

            #check the window size
            if right-left+1 == k:
                res.append(nums[q[0]])
                if q[0] == left:
                    q.popleft()#pop the left pointer's index from the queue because we are going to increment left pointer.
                left += 1

            right += 1

        return res          