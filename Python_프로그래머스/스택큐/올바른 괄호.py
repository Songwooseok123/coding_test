def solution(s):
    s_stack = []
    for i in s:
        if i =='(':
            s_stack.append(i)
        else:
            if s_stack== []:
                return False
            a= s_stack.pop()
            if a =='(':
                pass
            else:
                return False
        #print(s_stack)
    if s_stack == [] :
        return True
    else:
        return False
