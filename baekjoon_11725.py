from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = {key:[] for key in range(1, N + 1)}
parent = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
def dfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)
                
dfs()

for i in parent[2:]:
    print(i)