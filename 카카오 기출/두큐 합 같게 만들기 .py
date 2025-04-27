def solution(queue1, queue2):
    q = queue1 + queue2
    total = sum(q)
    
    if total % 2 != 0:
        return -1  # 전체 합이 홀수면 절대 같아질 수 없음
    
    target = total // 2
    
    left = 0
    right = len(queue1)
    current = sum(queue1)
    
    answer= 0
    flags = False
    while left<= right and right<len(q):
        
        if current == target :
            flags = True
            break
        elif current < target:
            current += q[right]
            right +=1
        else: 
            current-= q[left]
            left+=1
        answer +=1
    return answer if flags else -1