n = int(input())

def hanoi(n, start, target, sub):
    if n == 1:
        print(start, target)
    else:
        hanoi(n - 1, start, sub, target)
        print(start, target)
        hanoi(n - 1, sub, target, start)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 3, 2)