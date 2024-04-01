from itertools import permutations
def int_join(b):
    return int(''.join(b))
def get_SOSU(n):
    SOSU = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            SOSU.append(i)
            if i**2 !=n :
                SOSU.append(int(n/i))
    return len(SOSU) == 2
def solution(numbers):
    numberss = list(numbers)
    comb = []
    answer =0 
    for i in range(len(numberss)):
        comb.extend(list(permutations(numberss,i+1)))

    for i in list(set(map(int_join,comb))):
        if get_SOSU(int(i)):
            answer +=1
    
    return answer
