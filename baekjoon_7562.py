import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    if a == c and b == d:
        print(0)
        continue
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    s = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append([a, b])
    
    while q:
        x1, y1 = q.popleft()
      
        for i in range(8):
            x = x1 + dx[i]
            y = y1 + dy[i]
            if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
                visited[x][y] = 1
                s[x][y] = s[x1][y1] + 1
                q.append([x, y])
                
                if x == c and y == d:
                    break
    print(s[c][d])