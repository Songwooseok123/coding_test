import numpy as np
def solution(board, moves):
    board = np.array(board)
    basket = []
    count =0
    for i in moves: 

        target_line = board[:,i-1]
        #print("타겟라인",target_line)
        if sum(target_line) !=0:
            target_character = target_line[np.nonzero(target_line)[0][0]]
            basket.append(target_character)
            board[np.nonzero(target_line)[0][0],i-1] = 0
        else: 
            pass        
        #print("첫",basket)
        if len(basket)>1:
            if basket[-1] ==basket[-2]:
                count +=1
                del basket[-2:]
        #print("후",basket)
        #print(" ")
    return count*2

