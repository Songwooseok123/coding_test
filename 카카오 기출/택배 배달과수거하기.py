def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0  # 남은 배달 상자 수, 수거 상자 수
    
    for i in range(n-1, -1, -1):  # 맨 뒤(가장 먼 집)부터 앞으로
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:  # 배달이나 수거할게 남아있으면
            d -= cap  # 트럭 하나 가면서 배달 cap개 줄인다
            p -= cap  # 수거도 cap개 줄인다
            answer += (i + 1) * 2  # 거리 왕복 (i는 0-based라서 +1 해줘야 함)
            
    return answer
