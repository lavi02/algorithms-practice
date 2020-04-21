def solution(s):
    answer = True
    
    if 'p' in s or 'y' in s:
        if (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y')): answer = True
        else: answer = False
            
    elif 'p' not in s and 'y' not in s: answer = True
    
    

    return answer