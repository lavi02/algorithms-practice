word = input()
stack = [x for x in word]
queue = [x for x in word]

while stack:
    if stack.pop() != queue.pop(0):
        print(0)
        exit()
print(1)