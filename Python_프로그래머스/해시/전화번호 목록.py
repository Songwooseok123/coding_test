# 내 답안 시간초과 
## n^2k
def solution(phone_book):
    answer = True
    phone_book.sort(key = len)
    for i in range(len(phone_book)-1):
        for j in phone_book[i+1:]:
            if phone_book[i] == j[:len(phone_book[i])]:
                answer = False
                break
    return answer

# 모범답안 1 
## sorting을 해놨기 때문에 2번째 for 문을 돌릴 필요 없이 바로 다음 요소와 비교하면됨.  
## nlogn + nk
def solution(phone_book):
    phone_book.sort() # nlogn 
    for i in range(len(phone_book)-1): #n
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]: 
            return False 
    return True

# 모범답안 2 
## zip 함수 활용해서 모법답안 1 코드 짜기
def solution(phone_book):
    phone_book.sort() # nlogn
    for p,q in zip(phone_book,phone_book[1:]):
      if q.startswith(p):
        return False
    return True

# 모범답안 3 ## 이게 해시맵을 사용하는게 진짜 정답임 복잡도 n +nk
def solution(phone_book):
  hash_map = {}
  for i in phone_book:
      hash_map[i] =1
  for nums in phone_book:
      arr  = ""
      for num in nums:
          arr +=num
          if arr in hash_map and arr !=nums:
            return False
  return True
      
      
  
