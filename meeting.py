"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def canAttendMeetings(intervals) -> bool:
    if not intervals:
        return True
    intervals.sort(key=lambda x:x.start)

    prev_end = intervals[0].end
    for i in range(1, len(intervals)):
        if prev_end > intervals[i].start:
            return False
        else:
            prev_end = intervals[i].end
    return True