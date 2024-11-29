class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]

        while slow != slow2:#check if they are equal initally itself
        #because if start of the cycle itself is at nums[0] then we need to return that as duplicate not the next nums[slow] or nums[slow2]
            slow = nums[slow]   # Move both pointers by 1 step
            slow2 = nums[slow2]

        return slow
        