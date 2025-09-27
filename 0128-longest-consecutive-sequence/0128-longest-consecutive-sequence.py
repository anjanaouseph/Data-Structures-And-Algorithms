class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #brute force solution
        if len(nums) == 0:
            return 0

        arr_sorted = sorted(set(nums)) #O(nlogn)
        max_count = count = 1

        for i in range(len(arr_sorted)-1):
            if arr_sorted[i+1] == arr_sorted[i]+1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1

        return max_count