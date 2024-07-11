# 나의 풀이 - 시간복잡도 탈락 

from itertools import permutations
def divisors(n):
    divisors = []
    for i in range(1,n+1): 
        if n%i == 0:
            divisors.append(i)
    return len(divisors)

def solution(numbers):
    ## block 1(순열구하기)
    aaa =[]
    for i in range(len(numbers)):
        aaa.extend(list(map(''.join,list(permutations(numbers,i+1)))))
    

    ## block 2(0 제외랑 중복 제외)
    aaa= list(set(aaa))
    for i in range(len(aaa)):
        if aaa[i][0]=='0':
            if len(aaa[i])>1:
                aaa[i] = aaa[i][1:]
    aaa= list(set(aaa))

    answer = 0
    for i in aaa:
        
        if divisors(int(i)) ==2:
            answer +=1
    
    return answer

# 약수 구하는 코드 O(n)에서 O(n**0.5)으로 수정했는데도 시간복잡도 탈락. 
## 복잡 줄인거 
def divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1): 
        if n%i == 0:
            divisors.append(i)
            if i**2 !=n:
                divisors.append(int(n/i))
    return len(divisors)

# 모범답안 aaa= list(set(map(int,aaa)))로 block 2(0 제외랑 중복 제외)  개선하니 통과 
aaa = list(set(map(int,aaa)))

# 더 줄일 수 있음. 약수의 갯수 세지말고 2부터 약수가 구해지면 False 때려버리는 거임 
## 전체 코드
from itertools import permutations
def divisors(n):
    for i in range(2,int(n**0.5)+1): 
        if n%i == 0:
            return False # 함수는 return 만나면 걍 끝남. 
    if n not in [0,1]:
      return True
def solution(numbers):
    #순열구하고
    aaa =[]
    for i in range(len(numbers)):
        aaa.extend(list(map(''.join,list(permutations(numbers,i+1)))))
    # 정수화 + 중복제거 
    aaa = list(set(map(int,aaa)))
    # 1말고 약수 있는지 구하고
    answer = 0
    for i in aaa:
        if divisors(int(i)) :
            answer +=1
    
    return answer
