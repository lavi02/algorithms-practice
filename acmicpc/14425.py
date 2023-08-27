n, m = map(int, input().split())
strings = set(x for x in [input() for _ in range(n)])
count = 0

for _ in range(m):
    if input() in strings:
        count += 1

print(count)