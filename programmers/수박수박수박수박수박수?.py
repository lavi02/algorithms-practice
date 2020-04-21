def solution(n):
    data = ['수', '박']
    answer = ''
    
    for i in range(n):
        answer = answer + data[(i % 2)]
    
    return answer