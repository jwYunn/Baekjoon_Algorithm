N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False for _ in range(M + 1)] for __ in range(N + 1)]

dp[0][S] = True

for i in range(N):
    for j in range(M + 1):
        if not dp[i][j]:
            continue
        if j + V[i] <= M:
            dp[i + 1][j + V[i]] = True
        if j - V[i] >= 0:
            dp[i + 1][j - V[i]] = True
            


for i in range(M, -1, -1):
    if dp[N][i]:
        print(i)
        exit(0)
        
print(-1)