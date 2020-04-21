def solution(arr):
    answer = []
    i = 0.2
    
    for x in arr:
        if x != i:
            answer.append(x)
            i = x
    
    return answer