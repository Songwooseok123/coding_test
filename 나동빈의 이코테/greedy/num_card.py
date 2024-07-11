n, m = map(int, input().split())
datas = []
for i in range(n):
  data = map(int, input().split())
  min_value = min(data)
  datas.append(min_value)
print(max(datas))
#복잡도 n * m(개중에 최소값찾기)
