class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[""]]

        hashMap = collections.defaultdict(list)

        count = [0]*26

        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord('a')] += 1
            
            hashMap[tuple(count)].append(str)

        res = []

        for value in hashMap.values():
            res.append(value)

        return res        