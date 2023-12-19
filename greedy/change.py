# 거스름돈 
# 500, 100 ,50 , 10 무한개. n원 거슬러 줄 때 최소 동전의 갯수 (n:10의 배수) 
'''
1870원 -> 500원 3개, 100원 3개, 50원 1개, 10원 2개 
'''
n = 1870
coins = [500,100,50,10]
count = 0

for coin in coins : 
  count = count +(n//coin)
  n = n%coin



print(count)

