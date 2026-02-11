class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not order and not s:
            return ""

        hashMap = {}

        result = []

        for i in range(len(s)):
            ch = s[i]
            hashMap[ch] = hashMap.get(ch, 0)+1

        for i in range(len(order)):
            ch = order[i]

            while hashMap.get(ch, 0) != 0: #if ch is in order but not in s raises error
                result.append(ch)
                hashMap[ch] -= 1

        for key in hashMap.keys():
            while hashMap[key] != 0:
                result.append(key)
                hashMap[key] -= 1

        return "".join(result)
                

        





        