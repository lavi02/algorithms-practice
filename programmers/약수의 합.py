def solution(n):
    data = [0]
    for i in range(1, n + 1):
        if (n % i) == 0:
            data.append(i)
    
    answer = sum(data)
    return answer