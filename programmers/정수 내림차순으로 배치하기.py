def solution(n):
    data = []
    
    for x in str(n):
        data.append(x)
    
    data.sort(reverse = True)
    answer = ''.join(data)
    return int(answer)