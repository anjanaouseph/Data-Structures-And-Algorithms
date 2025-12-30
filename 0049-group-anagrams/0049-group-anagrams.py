from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return None

        hashMap = defaultdict(list)
        res = []

        for str in strs:
            #26 length array initialize
            key = [0]*26

            for char in str:
                key[ord(char)-ord('a')] += 1

            hashMap[tuple(key)].append(str)

        for key,values in hashMap.items():
            res.append(values)

        return res