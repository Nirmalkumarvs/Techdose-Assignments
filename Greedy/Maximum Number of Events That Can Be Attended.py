import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        ts_match = {}
        ts_beg, ts_end = 10 ** 6, 0
        
        for s, e in events:
            if s < ts_beg:
                ts_beg = s
            if e > ts_end:
                ts_end = e
            if s not in ts_match:
                ts_match[s] = [e]
            else:
                ts_match[s].append(e)
                
        res = 0
        earlist = []
        for t in range(ts_beg, ts_end + 1):
            
            if t in ts_match:
                for e in ts_match[t]:
                    heapq.heappush(earlist, e)
                
            if earlist:
                end = heapq.heappop(earlist)
                while earlist and end < t:
                    end = heapq.heappop(earlist)
                if end >= t:
                    res += 1
                    
        return res
