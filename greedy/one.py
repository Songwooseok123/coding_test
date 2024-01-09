# n = n-1
# n = n/k : n이 k로 나눠떨어질때만 
#n, k = map(int,input().split())
n,k = 26,3
count  = 0 
while True:
  target = (n//k) *k
  count += n- target #2
  n= target #24
  if n< k: 
    break
  count +=1 
  n= n//k  # 8 

count = count +(n-1) # 3+7


print(count)

