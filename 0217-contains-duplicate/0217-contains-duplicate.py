class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashMap = {}

        for num in nums:
            if not num in hashMap:
                hashMap[num] = 0

            hashMap[num] += 1

            if hashMap.get(num,0) > 1:
                return True

            
        return False