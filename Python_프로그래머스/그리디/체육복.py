def solution(n, lost, reserve):
    _lost = list(set(lost)-set(reserve))
    reserve = list(set(reserve)-set(lost))
    for i in reserve:
        if (i -1 in _lost) :
            _lost.remove(i-1)
        elif (i +1 in _lost) :
            
            _lost.remove(i+1)
    answer = n - len(_lost)
    return answer

