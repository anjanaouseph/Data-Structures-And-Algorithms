class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return [1]

        count = [[] for _ in range(len(nums)+1)] #indices represent the frequencies

        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 0

            hashMap[num] += 1


        for key,val in hashMap.items():
            count[val].append(key)

        key = k
        res = []

        for i in range(len(nums),0,-1):
            for freq in count[i]:
                if key:
                    res.append(freq)
                    key -= 1

        return res

        