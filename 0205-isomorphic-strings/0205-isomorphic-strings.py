class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap_s = {}
        hashMap_t = {}

        for i in range(len(s)):
            if s[i] in hashMap_s and hashMap_s[s[i]] != t[i]:
                return False #breach
            if t[i] in hashMap_t and hashMap_t[t[i]] != s[i]:
                return False

            hashMap_s[s[i]] = t[i]
            hashMap_t[t[i]] = s[i]

        return True       