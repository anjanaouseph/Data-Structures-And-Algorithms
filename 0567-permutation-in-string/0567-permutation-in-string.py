class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False

        map1 = [0]*26
        map2 = [0]*26

        for i in range(n1):
            map1[ord(s1[i])-ord('a')] += 1
            map2[ord(s2[i])-ord('a')] += 1

        if map1 == map2:
            return True

        l = 0
        r = n1
        while r<len(s2):
            map2[ord(s2[r])-ord('a')] += 1
            map2[ord(s2[l])-ord('a')] -= 1

            if map1 == map2:
                return True

            l += 1
            r += 1
        
        return False