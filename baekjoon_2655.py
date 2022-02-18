N = int(input())
array = []
array.append((0, 0, 0, 0))

dp = [0] * (N + 1)
index = 1

for _ in range(N):
    area, height, weight = map(int, input().split())
    array.append((index, area, height, weight))
    index += 1

array = sorted(array, key=lambda x : x[3])

for i in range(1, N + 1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])

max_value = max(dp)
index = N
result = []

while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1
    
print(dp)
result.reverse()
print(len(result))
[print(i) for i in result]    
