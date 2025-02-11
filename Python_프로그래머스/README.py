
# 정수 띄어쓰기로 input 받는거
list(map(int,input().split()))

# 시간초과 나면 input() 대신 sys.stdin.readline()을 시도해보자
a,b = map(int,sys.stdin.readline().split())
## 참고로 주피터에선 안됨 

# sort()를 len을 기준으로 할 수 있음
phone_book.sort(key=len)

# zip 함수 활용
phone_book =[1,2,3]
for p,q in zip(phone_book,phone_book[1:]):
  print(p,q)
  break
## 1,2

# phone_book[::-1]
## [3,2,1]

phone_book2 =[1,2,3]
#list(reversed(phone_book2))
## [3,2,1]

# 문자열 q가 p 문자열로 시작하는지
q.startswith(p)

# 리스트 요소 삭제 
## .remove(요소)- 처음 발견한(앞에서부터 탐색함) 1개만 삭제됨 
nums = [1,2,3,4,5]
nums.remove(2)
print(nums)
### [1, 3, 4, 5]
## .pop(n) - n번째 원소를 삭제하면서 삭제하는 요소 반환함 
```
nums = [1,2,3,4,5]
nums.pop(3)
print(nums)
# [1, 2, 3, 5]
```
# 요소 갯수세기 - dictionary 반환 
from collections import Counter
nums = [1,2,3,2,3]
numsss = [1,2,3,4,3,3]

Counter(nums)
## Counter({3: 3, 2: 2, 1: 1, 4: 1})
Counter(nums)
## Counter({3: 3, 1: 1, 2: 1, 4: 1})

## Counter 끼리 연산도 가능
Counter(nums) - Counter(numsss)
### Counter({2: 1})

## Counter해서 가장 많이 등장하는 n개 찾기 - 리스트 안에 튜플로 반환
nums = [1,2,3,2,3,5,5,5]
b = Counter(nums)
b.most_common(2)
### [(5, 3), (2, 2)]

# 순열과 조합 
from itertools import comninations,permutations # 순서대로 조합과 순열 
list(combinations(nums,2))

# set끼리 연산 가능 
set([1,2,3,3,3]) - set([1,3,4])
## {2}

# 리스트 2개로 dic만들기 
genres= ["cla", "pop", "sic", "ass"]	
plays= [500, 600, 150, 800]
{k:v for k,v in zip(genres,plays)}
## {'cla': 500, 'pop': 600, 'sic': 150, 'ass': 800}

# list 2개로 hashmap 만들기
## hashmap은 hashtable이라고도 불리고, 파이썬의 dictionary또한 hashtable로 구현되어있다. key와 value 쌍으로 데이터를 저장하는 자료구조를 말한다.
genres= ["cla", "pop","cla","sic" "sic", "ass"]	
plays= [500, 600, 150, 800,400,300]
hash_maps = {}
for i in range(len(genres)):
  if genres[i] in hash_maps:
    hash_maps[genres[i]].append(plays[i])
  else:
    hash_maps[genres[i]] = [plays[i]]
## {'cla': [500, 150], 'pop': [600], 'sicsic': [800], 'ass': [400]}


# 딕셔너리.keys(), 딕셔너리.values() ,딕셔너리.items()
# 딕셔너링 sort
sorted(hash_maps)
# key만 sort되서 나옴

sorted(hash_maps.items(),key = lambda x: sums[x[0]])
# hash_map을 정렬할건데... sums[x[0]] 함수의 결과값을 기준으로 정렬... x는 hash_maps.items()의 요소가 차례대로들어감
## 예를 들어 
a = {'cla': 500, 'pop': 600, 'sic': 150, 'ass': 800}
b= sorted(a.items(),key = lambda x: x[1])
b
# [('sic', 150), ('cla', 500), ('pop', 600), ('ass', 800)]

sorted_a = {k:v for k,v in b}
## {'sic': 150, 'cla': 500, 'pop': 600, 'ass': 800}

# continue 사용법
## if 문 만족하면 해당 i에 대한 for문이 끝나고 다음 i로 넘어감
## if 문 만족 안하면 밑에 print 실행함

arr = [1,1,3,3,0,1,1] 
for i in arr:
    if i==1:
        continue
    print(i,"야호")
## 3 야호
## 3 야호
## 0 야호

# 문자열 TO 숫자열 
ord('a')

# 빈리스트에 요소 있는지 확인할 때, 비어있을 때 error 뜸...이럴때 편법
answer = []
answer[-1] = i # error
answer[-1:] == [i] # 이런식으로 확인하면됨. 

# 요소 이어 붙히기
''.join(nums)

# 문자열 data가 문자인지 아닌지
data.isalpha()





