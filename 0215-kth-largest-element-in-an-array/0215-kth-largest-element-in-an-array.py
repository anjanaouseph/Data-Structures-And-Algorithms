class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #using hashMap and bucketsort
        if not nums:
            return -1

        hashMap = defaultdict(int)

        max_freq, min_freq = float(-inf), float(inf)

        for i in range(len(nums)):
            hashMap[nums[i]] += 1
            max_freq = max(max_freq, nums[i])
            min_freq = min(min_freq, nums[i])

        count = 0

        for i in range(max_freq, min_freq-1, -1): #bucket sort
            count += hashMap[i]
            if count >= k:
                return i

        return count       