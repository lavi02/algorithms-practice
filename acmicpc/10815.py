import sys
input = sys.stdin.readline

n = int(input())
used = sorted(list(set([int(x) for x in input().split()])))
m = int(input())
check = [int(x) for x in input().split()]

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

for i in check:
    if search(used, i):
        print(1, end=' ')
    else:
        print(0, end=' ')
