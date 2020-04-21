def solution(answers):
    first = [
        1, 2, 3, 4, 5
    ]
    
    second = [
        2, 1, 2, 3, 
        2, 4, 2, 5
    ]
    
    third = [
        3, 3, 1, 1, 2,
        2, 4, 4, 5, 5
    ]
    
    data = [
        0, 0, 0
    ]
    
    answer = []
    
    for x in range(0, len(answers)):
        if first[x % 5] == answers[x]: data[0] += 1          
        if second[x % 8] == answers[x]: data[1] += 1   
        if third[x % 10] == answers[x]: data[2] += 1
            
    MaxScore = max(data)
    
    if data[0] == MaxScore: answer.append(1)
    if data[1] == MaxScore: answer.append(2)
    if data[2] == MaxScore: answer.append(3)
            
    return answer