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

        #create pattern's adj list. m patterns per word, each costing O(m) to build.
        for word in wordList: #O(n*m^2) for every word it will generate m patterns, which costO(m), space complexity also same O(m*m*n)
            for j in range(len(word)): #m patterns
                pattern = word[:j]+"*"+word[j+1:] #O(m)
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
                            queue.append((nei, res+1))
                            visited.add(nei)

                    neighbors[pattern] = []

        return 0

# adj list:
# time complexity is O(m*m*n)
# space complexity is no of unique keys. Number of keys: O(n * m).Each key costs O(m) space. Keys space = O(n * m^2)
# Keys: O(n * m^2)
# Values: O(n * m) so dominant term is keys.

# BFS:
# Time = O(n · m²) 

# So worst case:
# n BFS words
# each word generates m patterns
# each pattern list may take up to O(n)
# That gives:
# For each visited word:
# generate m patterns → O(m^2)
# scan neighbors for each of the pattern →  O(mn) each pattern can have n words

# So per word:

# O(m^2 + mn)
# If BFS visits up to n words, total is:
# Time complexity of the BFS part:
# O(nm^2 + n^2m) = O(n^2 m)
# Space: O(n) queue can store n words worse case

# but with optmized BFS that is clearing the bucket after first scan, then
# Full BFS after optimization

# For each visited word:

# generate m patterns
# each pattern creation costs O(m)

# So pattern creation total:

# O(n * m^2)

# Neighbor scanning total:

# each bucket processed once overall
# total stored entries across all buckets = n * m
# so O(n * m)

# Total BFS:

# O(n * m^2 + n * m)
# simplifies to O(n * m^2)