class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #first optimized solution using sliding window

        l,r = 0,0
        max_freq, max_length = 0,0
        map = [0]*26#O(26) space complexity

        while r < len(s):
            map[ord(s[r]) - ord('A')] +=  1
            max_freq = max(max_freq, map[ord(s[r])-ord('A')])

            if (r-l+1 - max_freq) > k:#when the charaters to replace exceeds K
                map[ord(s[l])-ord('A')] -= 1 #we decrease the count
                #dont recalculate max_freq here again because decreasing that is pointless so
                #like this we can remove o(26) dependency, makes it a bit faster.
                l += 1 #shrink the window

            if r-l+1 - max_freq <=k :
                max_length = max(max_length, r-l+1) #calculate max length
                r += 1

        return max_length
        #Time Complexity is O(n)+O(n)*O(26) which is  O(n)+O(n)*O(1) which is O(n)