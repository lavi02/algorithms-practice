import sys
input = sys.stdin.readline

n = int(input())
temp = set()

for _ in range(n):
    a, b = input().split()

    if b == 'enter':
        temp.add(a)
    else:
        temp.remove(a)

print('\n'.join(sorted(temp, reverse=True)))