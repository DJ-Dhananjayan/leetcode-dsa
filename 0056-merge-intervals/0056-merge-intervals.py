class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    
        merge=[]
        intervals.sort(key=lambda x: x[0])
        prev=intervals[0]
        for  i in intervals[1:]:
            if i[0]<=prev[1] :
                prev[1]=max(i[1],prev[1])
            else :
                merge.append(prev)
                prev=i
        merge.append(prev)
        return merge












'''

        merged = []
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        merged.append(prev)
        return merged

'''