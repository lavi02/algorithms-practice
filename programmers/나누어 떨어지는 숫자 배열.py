def solution(arr, divisor):
    answer = []
    # sort - 오름차순, sort(diverse = True) - 내림차순
    
    for i in arr:
        if i % divisor == 0: answer.append(i)
            
    if len(answer) == 0: answer.append(-1)
    answer.sort()
    
    return answer