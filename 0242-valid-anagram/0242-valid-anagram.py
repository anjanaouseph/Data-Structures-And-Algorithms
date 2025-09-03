class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashMap1 = {}
        hashMap2 = {}

        for i in s:
            if not i in hashMap1:
                hashMap1[i] = 0

            hashMap1[i] += 1


        for i in t:
            if not i in hashMap2:
                hashMap2[i] = 0

            hashMap2[i] += 1

        if hashMap1 == hashMap2:
            return True

        return False