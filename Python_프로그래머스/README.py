
# 정수 띄어쓰기로 input 받는거
list(map(int,input().split()))

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
# 문자열 q가 p 문자열로 시작하는지
q.startswith(p)

# 리스트 요소 삭제 
## .remove(요소)- 처음 발견한(앞에서부터 탐색함) 1개만 삭제됨 
nums = [1,2,3,2,3]
nums.remove(2)
## .pop(n) - 뒤에서 n번째 1개 삭제하면서 삭제하는 요소 반환함 


# 요소 갯수세기 - dictionary반환(많은 요소부터 정렬해서 반)
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
b = Counter(nums)
b.most_common(2)
[(3, 3), (1, 1)]

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
genres= ["cla", "pop","cla","sic" "sic", "ass"]	
plays= [500, 600, 150, 800,400,300]
hash_maps = {}
for i in range(len(genres)):
  if genres[i] in hash_maps:
    hash_maps[genres[i]].append(plays[i])
  else:
    hash_maps[genres[i]] = [plays[i]]
## {'cla': [500, 150], 'pop': [600], 'sicsic': [800], 'ass': [400]}


# 딕셔너리.keys(), 딕셔너리.values() ,딕셔너리.items
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

# stask(선입후출), que(선입선출, 즉 대기줄)
## stack은 걍 리스트로구현, que는 collections의 deque로 구현
### deque(), popleft()
from collections import deque
ddd= deque()
ddd.append(5)
print(ddd)
ddd.append(4)
print(ddd)
ddd.append(3)
print(ddd)
ddd.popleft()
print(ddd)
'''
deque([5])
deque([5, 4])
deque([5, 4, 3])
deque([4, 3])
'''





 

