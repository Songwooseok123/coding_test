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
