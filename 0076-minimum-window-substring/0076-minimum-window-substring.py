class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ""

        #hashmap for t

        hashMap_T = defaultdict(int)

        for ch in t:
            hashMap_T[ch] += 1

        need = len(hashMap_T) #always unique element count because we later check actual frequencies
        have = 0

        hashMap_S = defaultdict(int)

        left,right = 0,0

        res, length = [-1, -1], float('inf') #window size, max length can go, we need min window length so we compare with inf

        while right < len(s):

            hashMap_S[s[right]]+=1
            ch = s[right]

            if ch in hashMap_T and hashMap_T[ch] == hashMap_S[ch]:
                have += 1

            #condition is satisfied we have found a window but we shrink it to see if we can find a smaller window
            while need == have:
                if right-left+1 < length:
                    res = [left, right+1] #update the smallest window length
                    length = right-left+1

                ch = s[left]
                hashMap_S[ch] -= 1
                if ch in hashMap_T and hashMap_S[ch] < hashMap_T[ch]:
                    have -= 1

                left += 1

            right += 1

        return s[res[0]: res[1]] if length > 0 else ""