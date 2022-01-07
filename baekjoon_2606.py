import sys
input = sys.stdin.readline

def bfs(start_node):
    visited, need_visited = [], []
    
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(gragh[node])
        
    return len(visited) - 1

N = int(input())
V = int(input())

gragh = {key:[] for key in range(1, 101)}

for _ in range(V):
    a, b = map(int, input().split())
    
    gragh[a].append(b)
    gragh[b].append(a)
    
print(bfs(1))