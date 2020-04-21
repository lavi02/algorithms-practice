def solution(array, commands):
    answer = []
    
    for x in range(0, len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        
        data = array[i - 1 : j]
        data.sort()
        answer.append(data[commands[x][2] - 1])
    
    return answer