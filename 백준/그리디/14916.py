#14916 그리디
n = int(input())

count = 0
found = False
while n>=0:
    if n%5 == 0:
        count += n//5
        found = True
        break
    else:
        n-=2
        count+=1
if found :
    print(count)
else:
    print(-1)
