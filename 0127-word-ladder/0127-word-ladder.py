class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #brute force
        # Map this to graph. Each word can be treated as a node, and I draw an edge between two nodes if the words differ by one letter. Since I want the shortest sequence of transformations, this becomes a shortest path problem in an unweighted graph.
        # each word that differ by 1 put into a queue, mark as seen and pop one by one while scanning the array for other words that differ by 1. so time complexity is O(n^2 * m). Even though you skip visited words, you still have to check every word to decide:Has it been visited?
# Each word is: pushed into the queue once. popped from the queue once
# Because you mark words as visited, you never process the same word twice.
# So: Total number of while loop iterations = at most n
        #more optimized approach is as below:
        # for every word, create all possible patterns it can generate and create an adj list, add all the words that come under this pattern to it. All these words are neighbors which differ by 1 unit. Then do BFS one by one.
        if endWord not in wordList: #O(N)
            return 0

        neighbors = defaultdict(list)

        queue = deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)

        #create pattern's adj list
        for word in wordList: #O(n*m^2) for every word it will generate m*m patterns, space complexity also same O(m*m*n)
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                neighbors[pattern].append(word)

        
        while queue: #here nodes will be patterns and edges will be connections to the words O(V+E) v is nodes or m*m and edges will be ...
        #space complexity will be ?
            for i in range(len(queue)):
                word, res = queue.popleft()

                if word == endWord:
                    return res

                #for this word create the patters and add the unvisited neighbors to the queue
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for nei in neighbors[pattern]:
                        if nei not in visited:
                            queue.append([nei, res+1])
                            visited.add(nei)

        return 0