class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x : x[0]) #sort based on first element of each list
        #O(nlogn)

        merged = []

        for i in range(len(intervals)):
                if merged and intervals[i][0] >= merged[len(merged)-1][0] and intervals[i][0] <= merged[len(merged)-1][1]:
                   x,y= merged.pop()
                   merged.append([x, max(y, intervals[i][1])])
                   i += 1
                else:
                    merged.append(intervals[i])
            

        return merged

        