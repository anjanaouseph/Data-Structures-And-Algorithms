class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {}
        
        for str in strs:
            count = [0]*26
            for char in str:
                count[ord(char)-ord('a')] += 1
            map.setdefault(tuple(count),[]).append(str)

        return map.values()    