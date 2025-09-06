class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [1]

        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0

            hashMap[num] += 1

        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)#this is tuples

        count = k

        res = []

        for i in range(count):
            res.append(sorted_items[i][0])

        return res
