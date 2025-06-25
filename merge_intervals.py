def merge(intervals):
    
    intervals.sort()

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])

    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))