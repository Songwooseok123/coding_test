## 내 답안 시간 초과 
def solution(nums):
    k  = int(len(nums)/2) 
    nums.sort()
    from collections import Counter
    a= Counter(nums)
    mmm = a.most_common(1)[0][0]
    while mmm in nums:
        nums.remove(mmm)
    from itertools import combinations
    answer = max(list(map(len,list(map(set,combinations(nums,k-1))))))+1
    return answer

## 모범 답안 

def solution(nums):
    k = len(nums)/2
    kk = len(set(nums))
    answer = min(k,kk)
    return answer

