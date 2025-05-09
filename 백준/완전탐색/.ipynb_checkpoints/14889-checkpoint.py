#14889 완전탐색
n = int(input())
board = []

for i in range(n):
    a = list(map(int,input().split()))
    board.append(a)

from itertools import combinations,permutations
aa= list(combinations(list(range(1,n+1)),n//2))
team1 = aa[:len(aa)//2]
team2 = aa[len(aa)//2:][::-1]

answer = 1e9
for a,b in zip(team1,team2):
    #print(a)
    #print(b)
    team1_sum, team2_sum = 0,0
    for s1,s2 in list(permutations(a,2)):
        team1_sum += board[s1-1][s2-1]
    for s1,s2 in list(permutations(b,2)):
        team2_sum += board[s1-1][s2-1] 
    candi = abs(team1_sum-team2_sum)
    answer = min(answer,candi)
print(answer)