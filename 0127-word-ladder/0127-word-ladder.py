class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0

        L = len(beginWord)

        q = deque([(beginWord, 1)])

        visited = set()

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            w = list(word) #list of word

            for i in range(L):
                original = w[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue
                    w[i] = c
                    next = "".join(w) #convert back to string
                    if next in word_set and next not in visited:
                        visited.add(next)
                        q.append((next, dist+1))

                w[i] = original

        return 0    