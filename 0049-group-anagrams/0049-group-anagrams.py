class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for str in strs:
            count = [0]*26

            for char in str:
                count[ord(char)-ord('a')] += 1

            key = tuple(count) 

            if key not in hashMap:
                hashMap[key] = []

            hashMap[key].append(str)

        result = []

        for key,value in hashMap.items():
            result.append(value)

        return result