class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        hashMap = {}
        res = []

        for str in strs:
            count = [0]*26

            for ch in str:
                count[ord(ch)-ord('a')] += 1

            key = tuple(count)
            if key not in hashMap:
                 hashMap[key] = []
            hashMap[key].append(str)

        for key,values in hashMap.items():
            res.append(values)
        
        return res      