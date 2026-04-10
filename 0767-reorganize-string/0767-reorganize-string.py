import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        #greedy + heap
        #why greedy? No two adjacent characters should be the same. This is a local constraint
    #    You only care about the next placement. At each step, what is the best choice I can make right   now? Place the character with highest remaining frequency (but not the same as last)
    #    Greedy Because:
    #     You make a locally optimal choice
    #     Without needing to reconsider past decisions
    #     And it leads to a valid global solution
    # Backtracking?
    # Try all permutations → too slow (n!)
    # No need to explore all possibilities
    # DP?
    # No overlapping subproblems
    # No need to store states
    #This is greedy because at each step we choose the most frequent valid character, ensuring optimal distribution without needing to revisit previous choices.
#    Brute Force Generate all permutations of the string. For each permutation:Check if any adjacent chars are same. Return the first valid one O(n!)
#using a hashmap to store char and their frequencies and then cycling through them won't work.aaabc,
# abcaa is wrong so hashmap + cycling wont work. we need abaca.
        hashMap = defaultdict(int)

        for ch in s:
            hashMap[ch] += 1

        prev = None
        res = ""

        max_heap = [(-values, key) for key,values in hashMap.items()]
        heapq.heapify(max_heap)

        while max_heap or prev: #O(n) we are building string char by char
            #base
            if not max_heap and prev:#means no elements exist in heap to pop and add to res
                return "" #we cant form the required string

            curr,key = heapq.heappop(max_heap) #O(log26)
            curr = curr+1 
            res += key

            if prev:
                heapq.heappush(max_heap,prev) #O(log26)
                prev = None

            if curr != 0:
                prev = (curr, key)
        
        return res

# Time Complexity is O(nlog26) = O(n)
# Space Complexity is O(n) = O(26)
#same logic we can scan hashmap each time instead of using heap