def solution(strings, n):
    answer = []
    alphabet = []
    repl = {}
    
    for i in strings:
        data = list(i)
        alphabet.append(data[n])
        alphabet.sort()
        
    for x in strings:
        data = list(x)
        for j in range(0, len(strings)):
            if data[n] == alphabet[j]: repl[j + 1]: x
        
    return answer