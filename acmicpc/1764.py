import sys
input = sys.stdin.readline

n, m = map(int, input().split())
isInList = set()

for _ in range(n):
    isInList.add(input().rstrip())

count = 0
people = []
for _ in range(m):
    inputData = input().rstrip()
    if inputData in isInList:
        count += 1
        people.append(inputData)

print(count)
print('\n'.join(people))