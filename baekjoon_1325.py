from collections import deque
import sys
input = sys.stdin.readline

def bfs(num):
    q = deque()
    q.append(num)
    visited = [0] * (n + 1)
    visited[num] = 1
    count = 1
        
    while q:
        node = q.popleft()
        for e in graph[node]:
            if not visited[e]:
                q.append(e)
                visited[e] = 1
                count += 1
            
    return count            

n, m = map(int, input().split())
graph = {key:[] for key in range(1, n + 1)}
result = []
max_count = -1

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    
for i in range(1, n + 1):
    count = bfs(i)
    
    if max_count < count:
        max_count = count
        result = [i]
    elif max_count == count:
        result.append(i)
    
for e in result:
    print(e, end=' ')