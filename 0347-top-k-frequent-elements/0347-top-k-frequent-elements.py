class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        hashMap = defaultdict(int)
        
        result = []
        
        max_val = 0
        min_val = float('inf')
        
        for num in nums:
            hashMap[num] = hashMap.get(num,0)+1
            max_val = max(hashMap[num], max_val)
            min_val = min(hashMap[num], min_val)
            
        
        # 1:3 2:2 3:1
        bucket_freq = [[] for _ in range(len(nums) + 1)]

         
        for key,value in hashMap.items():
            bucket_freq[value].append(key)
 
            
        count = k
            
        for i in range(max_val, -1, -1):
            if bucket_freq[i] and count > 0:
                for freq in bucket_freq[i]:
                    if count>=0:
                        result.append(freq)
                        count -= 1
                    
        return result
    
    #meeting room