def solution(n):
    answer = n ** 0.5
    
    if int(answer) == answer:
        return (int(answer) + 1) ** 2
    
    else:
        return -1