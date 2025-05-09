#1182 완전탐색 
# 수열의 부분 수열 중에서 합이 s를 만족하는 경우의 수 
n, s = list(map(int, input().split()))
array = list(map(int, input().split()))

from itertools import combinations
count =0
for k in range(1,n+1):
    for j in list(combinations(array,k)):
        
        if sum(j) == s:
            count+=1
print(count)