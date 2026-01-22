class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #brute force solution
        #create a freq map, then overwrite the array but O(n) space

        slow = 0 #this is to re-write the array
        fast = 0 #this is to iterate over the array

        count = 0

        while fast < len(nums):

            curr = nums[fast]

            while (fast < len(nums) and nums[fast] == curr): #so slow is a pointer which helps overwrite array, if u do nums[fast] == nums[slow], it can go to infinite loop in case like this [1 1 1 2 2 3], where slow = nums[2] = [1] and fast= nums[3] = [2], count = 0, both fast and slow won't incrementy. So infinite loop
                fast += 1
                count += 1

            jumps = min(count, 2)

            while jumps > 0:
                nums[slow] = curr
                slow += 1
                jumps -= 1

            count = 0

        return slow

    # Time Complexity: O(2N) = O(N)
    # Space Complexity: O(1)