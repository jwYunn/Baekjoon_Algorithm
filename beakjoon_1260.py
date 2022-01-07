import sys
input = sys.stdin.readline

def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))
    
    return visited

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
            
    return visited
    
N, M, V = map(int, input().split())
graph = {key:[] for key in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

print(*dfs(graph, V))
print(*bfs(graph, V))
