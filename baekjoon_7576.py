import sys
input = sys.stdin.readline

M, N = map(int, input().split())
s = []
q = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q_index = 0

for _ in range(N):
    row = list(map(str, input().split()))
    s.append(row)
    
for i in range(N):
    for j in range(M):
        if s[i][j] == '1':
            s[i][j] = 0
            q.append([i, j])

while q_index < len(q):
    a, b = q[q_index][0], q[q_index][1]
    
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        
        if 0 <= x < N and 0 <= y < M and s[x][y] == '0':
            s[x][y] = s[a][b] + 1
            q.append([x, y])
            
    q_index += 1
            
max_val = -1
for i in range(N):
    for j in range(M):
        if s[i][j] == '0':
            print(-1)
            exit(0)
        if s[i][j] == '-1':
            continue
        max_val = max(max_val, s[i][j])

print(max_val)