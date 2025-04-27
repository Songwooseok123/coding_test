def get_psum(a):

    psum =[0]*len(a)
    
    psum[0] = a[0]
    for i in range(1,len(a)):
        psum[i] = psum[i-1]+a[i]
    return psum
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    diff = [[0] * (m+1) for _ in range(n+1)]  # 누적합 배열 준비
    
    #print(diff)
    for type_, x1, y1, x2, y2, amount in skill:
        if type_ == 1:
            amount = -amount  # 공격이면 마이너스
        # 꼭짓점 4군데에 표시
        diff[x1][y1] += amount
        diff[x2+1][y1] -= amount
        diff[x1][y2+1] -= amount
        diff[x2+1][y2+1] += amount
    
    #print(diff)
    # 가로 누적합 (각 행에 대해 누적합 계산)
    for i in range(n):
        diff[i] = get_psum(diff[i])  # 각 행에 대해 누적합을 구함
    
    # 세로 누적합 (각 열에 대해 누적합 계산)
    for j in range(m):
        column = [diff[i][j] for i in range(n)]  # j번째 열을 추출
        column_psum = get_psum(column)  # 세로 누적합 계산
        for i in range(n):
            diff[i][j] = column_psum[i]  # 계산
    
    # board에 적용
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += diff[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
