#주어진 n개의 수를 m번 더해서 가장 큰 수를 만들자. 단 특정 인덱스 숫자 연속 k번 불가
# n m k : 5 8 3 
'''
12 4 -> 4 1 4 1 2
11 4 -> 4 1 4 1 1
10 4 -> 4 1 4 1 
9 4 -> 4 1 4 
8 4 -> 4 1 3 
7 4 -> 4 1 2
6 4 -> 4 1 1 
5 4 -> 4 1 
4 4-> 4 
'''

# 6 6 6 5 6 6 6 5 
#n,m,k = map(int,input().split())
#data = list(map(int,input().split()))
n,m,k = 5 , 8 ,3
data = [2,4,5,4,6]
data.sort()
#print(data)
#print(data[-1])
#print(data[-2])
cc = m//(k+1)
re = m%(k+1)
print((k*data[-1] + data[-2])*cc  + (data[-1]*re))
