import sys
input = sys.stdin.readline

n = int(input())
inputData = [x for x in map(int, input().split())]
inputData = list(set(inputData))
result = [0] * len(inputData)

for i in range(len(inputData)):
    count = 0
    for x in inputData:
        if inputData[i] > x:
            count += 1
    result[i] = count

print(*result)