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

        while hashMap or prev: #O(n) we are building string char by char
            #base
            if not hashMap and prev:#means no elements exist in heap to pop and add to res
                return "" #we cant form the required string

            candidate = None

            for ch in hashMap:
                if prev and ch == prev[0]:
                    continue
                if not candidate or hashMap[ch]>hashMap[candidate]:#find the most freq character
                    candidate = ch

            if candidate:
                res += candidate
            else:
                return ""

            hashMap[candidate] -= 1
            remaining = hashMap[candidate]

            if remaining == 0:
                del hashMap[candidate]

            if prev:
                hashMap[prev[0]] = prev[1]            
                prev = None

            if remaining > 0: #dont check hashMap[character] it returns 0 AND inserts the key back into the dictionary and hashMap never becomes empty due to defaultdict behavior.
                prev = (candidate, hashMap[candidate])
        
        return res

# Time Complexity is O(n*k) = O(n*26)
# Space Complexity is O(n) = O(26)
# The most frequent character is the hardest to place, so handle it early.