#Brute force is O(n3), so to optimize we need to use running sum/ prefix sum.
#The subarray between two same running sums is balanced.
#We need to find if the running sum has happened before so store the index.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hashMap = {0: -1}  #to store the earliest index

        prefix_sum = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in hashMap:#find the first index of sum if it exists
                max_len = max(max_len, i - hashMap[prefix_sum])
            else:
                hashMap[prefix_sum] = i

        return max_len    