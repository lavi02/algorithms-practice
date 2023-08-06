n = int(input())
total = len(str(n))
pos = n - 9*total

# 생성자는 이 안에 있음
found = False
for i in range(max(pos, 1), n):  # 0이 아닌 양수의 생성자만 고려
    sumData = i + sum(map(int, str(i)))
    if sumData == n:
        print(i)
        found = True
        break

if not found:
    print(0)
