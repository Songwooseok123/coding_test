# 15650 완전탐색 
a,b = list(map(int,input().split()))
from itertools import combinations

for j in list(combinations(list(range(1,a+1)),b)):
    print(*j)
