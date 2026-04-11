class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #Brute Force is O(n2) - generate all subarrays and use a set to check the occurance of more than two types of fruits and validate each substring.
        
        hashMap = defaultdict(int)

        max_len = 0

        left = 0
        right = 0

        for right in range(len(fruits)):

            hashMap[fruits[right]] += 1 #increase the freq

            while hashMap and len(hashMap) > 2:
                hashMap[fruits[left]] -= 1
                if hashMap[fruits[left]] == 0:
                    del hashMap[fruits[left]]
                #max_len = max(max_len, right-left+1)
                left += 1

            max_len = max(max_len,right-left+1)
            right += 1

        return max_len

# TC: O(N) each element added once and removed once so 2N = N
# SC: O(N)