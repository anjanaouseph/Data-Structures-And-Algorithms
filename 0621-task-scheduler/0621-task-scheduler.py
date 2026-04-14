class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #using heap and queue

        #create a hashMap
        hashMap = defaultdict(int)

        for task in tasks:
            hashMap[task] += 1

        #A : 3, B:3

        maxHeap = [-count for count in hashMap.values()] #for max heap we make it -ve

        heapq.heapify(maxHeap) #klogk
        #arranging by max freq first make sure we don't exhaust the required tasks letter.

        time = 0

        queue = deque()

        while maxHeap or queue: #Work per step = O(log U) You’re not iterating over tasks — you’re iterating over time
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap)+1
                if count:
                    queue.append((count, time+n)) #add to queue this freq and time it needs to wait
                
            if queue:
                if queue[0][1] == time: #time has come for the task to pop from the queue
                    heapq.heappush(maxHeap, queue.popleft()[0])

        return time        

# TC: O(T) T iterations × O(log U) U is a costant
# SC: O(1)  (since at most 26 tasks)