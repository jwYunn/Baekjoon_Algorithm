import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
s = []
q = deque()
q_index = 0
crush_q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result_list = []

for _ in range(N):
    row = list(input().strip())
    s.append(row)
    
s[0][0] = 1
crush_q.append([0, 0])

while q_index < len(crush_q):
    o, x = crush_q[q_index]
    sum = copy.deepcopy(s)
    if not(o == 0 and x == 0):
        sum[o][x] = '0'
    
    q.append([0, 0])
    print(crush_q)
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < N and 0 <= y < M and sum[x][y] == '0':
                q.append([x, y])
                sum[x][y] = sum[a][b] + 1
                
            if 0 <= x < N and 0 <= y < M and sum[x][y] == '1':
                if [x, y] not in crush_q:
                    crush_q.append([x, y])
    
    if sum[N - 1][M -1] != '0':
        result_list.append(sum[N - 1][M - 1])
        
    q_index += 1

if result_list:
    print(min(result_list))
else:
    print(-1)