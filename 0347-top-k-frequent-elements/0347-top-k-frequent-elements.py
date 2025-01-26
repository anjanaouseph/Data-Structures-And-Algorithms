class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        map = collections.defaultdict(int)

        for num in nums:
            map[num] = map.setdefault(num,0)+1

        #Frequencies are non negative
        freqs = [[] for _ in range(len(nums) + 1)]

        for key,val in map.items():
            freqs[val].append(key)

        result = []

        i = k
        
        for i in range(len(freqs)-1,-1,-1):
                for freq in freqs[i]:
                    result.append(freq)
                    if len(result)==k:
                        return result

        return result







        