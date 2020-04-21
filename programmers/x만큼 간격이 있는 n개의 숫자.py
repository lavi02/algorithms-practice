def solution(x, n):
    answer = []
    i = 0
    
    for a in range(n):
        i += x
        answer.append(i)
            
    return answer