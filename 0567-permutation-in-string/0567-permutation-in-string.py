class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #two hashmaps to store the frequency

        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:#if second string is smaller then definitely it won't exist.
            return False

        hashMap1 = [0]*26
        hashMap2 = [0]*26

        for i in range(n1):
            hashMap1[ord(s1[i])-ord('a')] += 1

        
        left = 0
        right = 0

        while right < n2:
            hashMap2[ord(s2[right])-ord('a')] += 1

            while right-left+1 > n1:#if condition also works here because if the window grows by 1 we shrink it.
                hashMap2[ord(s2[left])-ord('a')] -= 1
                left += 1
            
            if hashMap1 == hashMap2:
                return True

            right += 1

        return False