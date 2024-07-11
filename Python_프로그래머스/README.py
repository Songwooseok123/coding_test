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

# 문자열 q가 p 문자열로 시작하는지
q.startswith(p)

# 리스트 요소 삭제 - 처음 발견한(앞에서부터 탐색함) 1개만 삭제됨 
nums = [1,2,3,2,3]
nums.remove(2)

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
# {2}



 

