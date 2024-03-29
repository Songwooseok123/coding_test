def solution(s):
    
    num_str = ['zero','one','two','three','four','five'
          ,'six','seven','eight','nine']
    result = []
    string_repo = ''
    for i in s:
        if i.isdigit():
            result.append(str(i))
            print
        else:
            string_repo +=i
            if string_repo in num_str:
                result.append(str(num_str.index(string_repo)))
                string_repo = ''
    return int(''.join(result))
        
        
