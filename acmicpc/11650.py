import sys
input = sys.stdin.readline

n = int(input())
inputData = [[0, 0] for _ in range(n)]
for i in range(n):
    inputData[i] = list(map(int, input().split()))

inputData.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(inputData[i][0], inputData[i][1])