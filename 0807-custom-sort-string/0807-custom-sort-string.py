class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = defaultdict(int)

        for char in s:
            hashMap[char] += 1

        string_builder = []

        for char in order:
            if hashMap[char]:
                string_builder.append(char * hashMap[char])
                del hashMap[char] #to remove a key from hashMap if using collections

            
        for key,values in hashMap.items():
            string_builder.append(key * values)


        return ''.join(string_builder)    