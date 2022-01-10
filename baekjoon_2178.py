import sys
input = sys.stdin.readline

N, M = map(int, input().split())
q = [[0, 0]]
s = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    s.append(list(input())) 

s[0][0] = 1
    
while q:
    a, b = q[0][0], q[0][1]
    del q[0]
    
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        
        if 0 <= x < N and 0 <= y < M and s[x][y] == '1':
            q.append([x, y])
            s[x][y] = s[a][b] + 1

print(s[N - 1][M - 1])