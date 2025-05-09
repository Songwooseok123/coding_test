#2178 bfs 

n, m = list(map(int, input().split()))

a=[]
for i in range(n):
    a.append(input())

from collections import deque

visit=[[False]*m for _ in range(n)]
shortest_d = [[-1]*m for _ in range(n)]
queue = deque()

queue.append((0,0))
visit[0][0] = True
shortest_d[0][0] = 0

#print(visit)
#print(shortest_d)


while queue:
    r, c = queue.popleft()
    

    if r > 0 and a[r - 1][c] == '1' and not visit[r - 1][c]: # 윗방향
        queue.append((r - 1, c))
        visit[r - 1][c] = True
        shortest_d[r - 1][c] = shortest_d[r][c] + 1

    if r < n - 1 and a[r + 1][c] == '1' and not visit[r + 1][c]: #아랫방향
        queue.append((r + 1, c))
        visit[r + 1][c] = True
        shortest_d[r + 1][c] = shortest_d[r][c] + 1

    if c > 0 and a[r][c - 1] == '1' and not visit[r][c - 1]: # 왼방향
        
        queue.append((r, c - 1))
        visit[r][c - 1] = True
        shortest_d[r][c - 1] = shortest_d[r][c] + 1

    if c < m - 1 and a[r][c + 1] == '1' and not visit[r][c + 1]: # 오른방향 
        
        queue.append((r, c + 1))
        visit[r][c + 1] = True
        shortest_d[r][c + 1] = shortest_d[r][c] + 1
print(shortest_d[n-1][m-1]+1)

