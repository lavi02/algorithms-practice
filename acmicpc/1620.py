import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pockemon = {}

for i in range(1, n + 1):
    name = input().rstrip()
    pockemon[name] = i
    pockemon[str(i)] = name

for _ in range(m):
    inputData = input().rstrip()
    if inputData.isdigit():
        print(pockemon[inputData])
    else:
        print(pockemon[inputData])

