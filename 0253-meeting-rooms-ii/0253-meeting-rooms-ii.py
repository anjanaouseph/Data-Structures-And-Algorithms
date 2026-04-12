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
            
            res = max(res, count)

        return res

# TC: O(nlogn)
# SC: O(n)
