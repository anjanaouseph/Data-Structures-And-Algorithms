class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if  not beginWord or not endWord or not wordList:
            return 0

        hashMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]

                hashMap[pattern].append(word)

        #we do BFS as we want to find the shortest transformation sequence.

        visited = set()
        queue = deque([(beginWord, 1)])
        visited.add(beginWord)

        #BFS
        while queue:
            word, distance = queue.popleft()

            if word == endWord:
                return distance  

            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]

                potential_words = hashMap.get(pattern)

                if potential_words:
                    for potential_word in potential_words:
                        if potential_word not in visited:
                            queue.append((potential_word, distance+1))
                            visited.add(potential_word)

        return 0
        