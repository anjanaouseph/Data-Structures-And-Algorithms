class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1

        slow = nums[0] 
        fast = nums[0]

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast:#cycle detected
                break

        #now find the starting node of cycle

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow