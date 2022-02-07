from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph):
    count = 0
    visited = [0 for _ in range(len(graph.keys()) + 1)]
    for key in graph.keys():
        if visited[key] == 1:
            continue
        
        if len(graph[key]) == 0:
            count += 1
            visited[key] = 1
            continue
        
        q = deque()
        q.append(key)
        
        isCycle = False
        while q:
            node = q.popleft()
            if visited[node] == 1:
                isCycle = True
            visited[node] = 1
            for i in graph[node]:
                if visited[i] == 0:
                    q.append(i)
        if not isCycle:
            count += 1
            
    return count


if __name__ == "__main__":
    
    case = 1
    while True:
        n, m = map(int, input().split())
        
        graph = {key:[] for key in range(1, n + 1)}
        
        if n == 0 and m == 0:
            break
        
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
            
        result = bfs(graph)
        
        if result == 0:
            print(f"Case {case}: No trees.")
        elif result == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {result} trees.")
        
        case += 1