def solution(x):
    data = list(map(int, str(x)))
    
    if x % sum(data) == 0:
        return True
    
    else:
        return False