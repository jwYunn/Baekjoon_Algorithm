import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = {key:[] for key in range(1, N + 1)}
result = []

for _ in range(N):
    val = list(map(int, input().split()))
    
    for i in range(1, len(val) - 2, 2):
            graph[val[0]].append((val[i], val[i + 1]))
        
def dfs(node):
    q = deque()
    q.append(node)
    distance = [0 for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    
    visited[node] = 1
    
    while q:
        node = q.popleft()
        
        for n, v in graph[node]:
            if visited[n] == 0 and (distance[n] == 0 or distance[node] + v > distance[n]):
                visited[n] = 1
                distance[n] = distance[node] + v
                q.append(n)
    
    max_dis = max(distance)
    index = distance.index(max_dis)            
    return index, max_dis                 

index, value = dfs(1)
index, value = dfs(index)

print(value)