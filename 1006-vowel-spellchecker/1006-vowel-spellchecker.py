class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        #the key here is to make 3 lookup tables
        words_exact = set(wordlist) #hashset of unique words
        words_cap = {}
        words_vowel = {}

        for word in wordlist:
            #convert to lower case first
            word_lower = word.lower()
            words_cap.setdefault(word_lower, word) #should return the first such match in the wordlist.
            words_vowel.setdefault(self.toVowel(word_lower), word) #should return the first such match in the wordlist.
        result = []

        for query in queries:
            if query in words_exact:
                result.append(query)
                continue

            query_lower = query.lower()

            if query_lower in words_cap:
                result.append(words_cap[query_lower])
                continue

            if self.toVowel(query_lower) in words_vowel:#we need to check the devoweled query
                result.append(words_vowel[self.toVowel(query_lower)])
                continue

            result.append("")

        return result


    def toVowel(self, word):
        return "".join( "*" if c in "aeiou" else c for c in word)
