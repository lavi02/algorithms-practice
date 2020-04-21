input_data = []
input_data.append(int(input()))
data = {}

for x in range(0, input_data[0]):
    a, b = input().split()
    data.update({int(a): int(b)})
result = sorted(data)

for answer in result:
    var = data[answer]
    print("%d %d" % (answer, var))