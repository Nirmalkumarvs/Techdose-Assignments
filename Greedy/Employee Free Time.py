schedules=[[[1,2],[5,6]],[[1,3]],[[4,10]]]

def employeeFreeTime(schedule):
    if not schedule:
        return []

    intervals = []
    
    for employee in schedule:
        for interval in employee:
            intervals.append(interval[::])
            
    intervals.sort(key=lambda x:x[0])

    res =[]
    lastend = intervals[0][1]
    for start,end in intervals[1:]:
        if start > lastend:
            res.append([lastend, start])
        lastend = max(lastend, end)
    return res


print(employeeFreeTime(schedules))
