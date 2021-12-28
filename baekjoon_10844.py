import sys

input = sys.stdin.readline

n = int(input())
cost = []

cost.append(0)
for _ in range(n):
    value = int(input())
    cost.append(value)

if n < 3:
    print(sum(cost))
    exit(0)

s = [0] * (n + 1)

s[1] = cost[1]
s[2] = cost[2] + s[1]

for i in range(3, n + 1):
    s[i] = max(s[i - 1], s[i - 3] + cost[i - 1] + cost[i], s[i - 2] + cost[i])
    
print(max(s))