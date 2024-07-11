

# 모범답안
def solution(genres, plays):
    hash_maps = {}
    sum_maps={}
    for i,(gen,pla) in enumerate(zip(genres,plays)):
        if gen in hash_maps:
            hash_maps[gen].append((i,pla))
        else:
            hash_maps[gen] = [(i,pla)]
        if gen in sum_maps:
            sum_maps[gen] +=pla
        else: sum_maps[gen] = pla
    answer = []
    bb= sorted(sum_maps.items(), key=lambda x:x[1], reverse=True)
    for k,_ in bb:
        aa =sorted(hash_maps[k], key=lambda x:x[1], reverse=True)[:2] 
        answer.extend([j for j,_ in aa])
    return answer
