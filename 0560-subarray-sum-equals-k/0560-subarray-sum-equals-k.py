class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

       hashMap = collections.defaultdict(int)
       hashMap[0] = 1 

       running_sum = 0
       res = 0

       for num in nums:
            running_sum += num

            if hashMap[running_sum - k]:
                res += hashMap[running_sum-k]
                #running_sum-k can be zero when [1 2] and k = 3 to handle that we need to
                #set hashMap[0] = 1 

            hashMap[running_sum] += 1
       return res
