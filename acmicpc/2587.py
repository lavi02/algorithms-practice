data = []
avg = 0

try:
    while True:
        data.append(int(input()))
except:
    pass

data.sort()
avg = sum(data) // len(data)

print(avg)
print(data[len(data) // 2])