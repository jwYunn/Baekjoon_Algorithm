import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = {key:[] for key in range(1, n + 1)}
    
for _  in range(n - 1):
    super_node, sub_node, cost = map(int, input().split())
    graph[super_node].append((sub_node, cost))
    graph[sub_node].append((super_node, cost))
    
if n == 1:
    print(0)
    exit(0)
    
def dfs(num):
    q = deque()
    q.append(num)
    dis = [0 for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    
    visited[num] = 1
    
    while q:
        node = q.popleft()
        
        for i, j in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                dis[i] = dis[node] + j
                q.append(i)
    
    max_dis = max(dis)
    index = dis.index(max_dis)
    return index, max_dis

index, value = dfs(1)
index, value = dfs(index)
print(value)