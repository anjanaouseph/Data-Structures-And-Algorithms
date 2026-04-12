class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #At any point of time find the maximum no of overlapping meetings

        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        res = 0
        count = 0

        s = 0
        e = 0

        while s < len(intervals):
            if start[s] < end[e]:#meeting going on before end
                count += 1 #meeting going on before ending so need extra room
                s += 1

            else:#means A meeting ends before the next one starts
                count -= 1 #so free a room
                e += 1
                #if a meeting starts  when another ends, we can use same room so no need of extra room
            
            res = max(res, count)

        return res

# find all meetings which starts before first end time -> means meetings are going on in parallel
# finally you find a meeting which starts after the current end time. We have found all meetings that begin before the current end time so safe to move to the next end time. Since one meeting ended we can free up a room. All this logic works because we sorted the arrays.

# TC: O(nlogn)
# SC: O(n)
