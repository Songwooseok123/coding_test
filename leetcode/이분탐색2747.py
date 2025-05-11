# 밑에처럼 이분탐색으로 풀면 시간초과남 

from bisect import bisect_left, bisect_right

logs.sort(key = lambda x : x[1])
logss = [l[1] for l in logs]

cc = []
for q in queries:
    
    s,e = q -x, q
    low = bisect_left(logss,s)
    high = bisect_right(logss,e)
    set_log = set([i[0] for i in logs[low:high]])
    cc.append(n -len(set_log))
cc
## 모범답안은 따로 파일 있음.