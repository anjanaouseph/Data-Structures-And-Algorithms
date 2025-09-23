class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def toVowel(word):
            return "".join("*" if c in "aeiou" else c for c in word)

        #first we need 3 lookup tables

        words_exact = {}
        words_capital = {}
        words_vowel = {}

        words_exact = set(wordlist)
        
        for word in wordlist:
            word_lower = word.lower()

            # words_capital.setdefault(word_lower, word)
            # words_vowel.setdefault(toVowel(word_lower), word)
            if word_lower not in words_capital:
                words_capital[word_lower] = word

            if toVowel(word_lower) not in words_vowel:
                words_vowel[toVowel(word_lower)] = word
        
        ans = []

        for query in queries:
            query_lower = query.lower()

            if query in words_exact:
                ans.append(query)
                continue

            if query_lower in words_capital:
                ans.append(words_capital[query_lower])
                continue

            if toVowel(query_lower) in words_vowel:
                ans.append(words_vowel[toVowel(query_lower)])
                continue

            ans.append("")

        return ans