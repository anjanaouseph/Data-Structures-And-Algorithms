class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0]) #sort based on first element of each list
        #O(nlogn)

        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:#the first element is greater than the last element of the merged interval's range then no overlap
                merged.append(interval)
            else:
                 merged[-1] = [merged[-1][0],max(merged[-1][1], interval[1])]

        return merged
