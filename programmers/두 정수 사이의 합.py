data = []
result = 0

def function(x, y):
    global result

    for i in range(y - x + 1):
        data.append(x)
        x = x + 1
        
    result = sum(data)
    
    return result

def solution(a, b):
    global result
    if a < b:
        function(a, b)
        return result
    
    elif a == b:
        result = a
        return result
    
    else:
        function(b, a)
        return result