# 1759 완전탐색 
# 최소 1개 모음(aeiou)과 최소 두개 자음 -> 모음2개자음2개 or 모음1개자음3개 
# 오름차순 

l,c = list(map(int,input().split()))
s = list(input().split())

s.sort()
from itertools import combinations

for combination in combinations(s,l):
    m = 0
    z = 0
    for a in combination:
        if a in ['a', 'e', 'i', 'o', 'u']:
            m +=1
        else:
            z+=1
    if m>=1 and z>=2:
        print(''.join(combination))
    