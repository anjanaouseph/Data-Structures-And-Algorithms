class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        hashMap = {}
        min_key = max_key =0

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.setdefault(nums[i],0)+1
            min_key = min(min_key, nums[i])
            max_key = max(max_key, nums[i])

        sum = 0
        
        for key in range(max_key, min_key - 1, -1):#reverse loop
            sum += hashMap.get(key, 0)#if key exists else return 0
            if sum >= k:
                return key
        return 0     