import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    
    while q:
        v = q.popleft()
        if v == k:
            return visited[k]
        for i in (v-1, v+1, v*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, input().split())
visited = [0] * 100001
print(bfs(n))