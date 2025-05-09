# 22864 완전탐색
a, b, c, m = map(int, input().split()) # 피로도+, 일,피로도-, 피로도 한계 m 
# 얼마나 일을 할 수 있을까 

piro = 0
work =0
for i in range(24):
    if piro+a  <= m:
        piro +=a
        work +=1
    else:
        piro-=c
        piro = max(0,piro)


print(work*b)