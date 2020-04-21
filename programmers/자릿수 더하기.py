def solution(n):
    answer = 0
    data = list(str(n))
    
    for i in data:
        answer = answer + int(i)

    return answer