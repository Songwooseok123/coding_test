# 시간 초과 
def solution(participant, completion):
    for i in participant:
        print(i)
        if i in completion:
            completion.remove(i)
        else:
            #print(i,"adsfsaf")
            break
    answer = i
    return answer
# 답안 1 - n+m
from collections import Counter

def solution(participant, completion):
    counter = Counter(completion) # m
    for i in participant: #n
        if counter[i] > 0:
            counter[i] -= 1
        else:
            return i
# 답안 2 - nlogn
def solution(participant, completion):
	# 리스트를 이름 순으로 정렬
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
         # 순서가 맞지않으면 완주하지 못한 선수
        if participant[i] != completion[i]:
            return participant[i]
    # 위에서 순서가 다 맞았다면 마지막 선수가 완주하지 못한 선수        
    return participant[-1]
