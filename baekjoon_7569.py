import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
q_index = 0
s = []
q = []
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

for _ in range(H):
    temp = []
    for _ in range(N):
        row = list(map(str, input().split()))
        temp.append(row)
    s.append(temp)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if s[i][j][k] == '1': 
                s[i][j][k] = 0
                q.append([i, j ,k])

while q_index < len(q):
    a, b, c = q[q_index][0], q[q_index][1], q[q_index][2]
    
    for i in range(6):
        x = b + dx[i]
        y = c + dy[i]
        h = a + dh[i]
        
        if 0 <= x < N and 0 <= y < M and 0 <= h < H and s[h][x][y] == '0':
            q.append([h, x, y])
            s[h][x][y] = s[a][b][c] + 1
        
    q_index += 1

max_val = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if s[i][j][k] == '0':
                print(-1)
                exit(0)
            max_val = max(max_val, int(s[i][j][k]))
            
print(max_val)