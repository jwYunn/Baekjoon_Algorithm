N = int(input())
array = map(int, input().split())

array = sorted(array)

result = 0
value = 0

for i in array:
    value += i
    result += value
    
print(result)