# 2805  이분탐색
# 적어도 m 미터의 나무를 집에 가져가기위한 절단기의 최댓값
n, m = list(map(int, input().split()))
height = list(map(int, input().split()))
def get_height(mid):
    sum_h = 0
    for h in height:
        if h >mid:
            sum_h +=h-mid

    
    return sum_h


start = 0
end = max(height)
answer= None

while start<=end:
    mid = (start+end)//2
    getted = get_height(mid)
    #print(mid, getted)
    if getted < m:
        end = mid -1
    else: 
        start = mid+1
        answer = mid
print(answer)