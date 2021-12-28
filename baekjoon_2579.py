import sys

input = sys.stdin.readline

n = int(input())

cost = []
cost.append(0)
dp = [0] * (n + 1)

for _ in range(n):
    value = int(input())
    cost.append(value)
    
if n < 3:
    print(sum(cost))
    exit(0)
    
dp[1] = cost[1]
dp[2] = dp[1] + cost[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + cost[i - 1] + cost[i], dp[i - 2] + cost[i])
    
print(dp[n])