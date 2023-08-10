import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(input().rstrip())

data = list(set(data))
data.sort(key = lambda x: (len(x), x))
print('\n'.join(data))