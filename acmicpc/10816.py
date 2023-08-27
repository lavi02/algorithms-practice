import sys
input = sys.stdin.readline

n = int(input())
used = [int(x) for x in input().split()]
m = int(input())
check = [int(x) for x in input().split()]

used.sort()
count = {}

def search(i, x):
    left, right = 0, len(i) - 1
    while left <= right:
        mid = (left + right) // 2
        if i[mid] == x:
            return True
        elif i[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

for i in used:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(' '.join(str(count[x]) if x in count else '0' for x in check))

