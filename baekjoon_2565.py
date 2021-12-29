N = int(input())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

array.sort()

dp = [1] * N

for i in range(N):
    for j in range(i):
        if array[i][1] > array[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(N - max(dp)) 