"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #print(intervals[0].start)
        intervals.sort(key = lambda x : x.start)
        heap_ = []
        
        for interval in intervals:
            s,e = interval.start, interval.end
            if heap_:
                if heap_[0]<=s:
                    heappop(heap_)


            heappush(heap_,e)
        return len(heap_)
        