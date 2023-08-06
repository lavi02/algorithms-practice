n = int(input())
count = 0
# 5x + 3y = n

while n != 0:
    if n % 5 == 0:
        count += n // 5
        break
    elif n < 3:
        count = -1
        break
    n -= 3
    count += 1

print(count)