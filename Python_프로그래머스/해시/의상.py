import numpy as np
from itertools import combinations
def solution(clothes):
    a= np.array(clothes)[:,1]
    count = 0
    for i in range(len(clothes)):
        count +=len(list(j for j in list(map(np.unique, list(combinations(a,i+1)))) if len(j) ==i+1))
        #print(list(j for j in list(map(np.unique, list(combinations(a,i+1)))) if len(j) ==i+1))
    answer = count
    return answer
# 복잡도 너무 높음... combinations(n,k)의 복잡도는 n의 k승임 

# 모범답안 1
## 걍 예를 들어 바지 n개 상의 m개 있으면, (n+1)(m+1) -1 하면 답임... 
### n이랑 m만 구하면됨 

from collections import Counter

def solution(clothes):
    counter = Counter([category for _, category in clothes])
    #counter =  np.array(clothes)[:,1] # 바로 윗줄의 코드와 같은 코드임
    answer = 1
    for count in counter.values():
        answer *= (count + 1)
    return answer - 1
