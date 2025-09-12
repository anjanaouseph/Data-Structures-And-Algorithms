class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #sort the intervals first to handle cases [[4,7],[1,4]]
        intervals.sort(key = lambda x:x[0])

        merged = []

        for interval in intervals:
            if merged and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(interval[1],merged[-1][1])

            else:
                merged.append(interval)

        return merged
        