import sys
input = sys.stdin.readline

test_case = int(input())

def bfs(start_node):
    global temp
    global result
    visited, need_visited = [], []
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            if node not in temp:
                temp.append(node)
    result += 1
    return

for _ in range(test_case):
    M, N, K = map(int, input().split())
    
    graph = {(i ,j):[] for i in range(M) for j in range(N)}
    array = [[0 for _ in range(N)] for _ in range(M)]
    result = 0
    temp = []
    
    for i in range(K):
        a, b = map(int, input().split())
        array[a][b] = 1
    
    for i in range(M):
        for j in range(N):
            isSelected = False
            if array[i][j] == 1:
                if i > 0 and array[i - 1][j] == 1:
                    isSelected = True
                    graph[(i, j)].append((i - 1, j))
                    
                if i < M - 1 and array[i + 1][j] == 1:
                    isSelected = True
                    graph[(i, j)].append((i + 1, j))
                    
                if j > 0 and array[i][j - 1] == 1:
                    isSelected = True
                    graph[(i, j)].append((i,j - 1))
                    
                if j < N - 1 and array[i][j + 1] == 1:            
                    isSelected = True
                    graph[(i, j)].append((i,j + 1))
                    
                if not isSelected:
                    result += 1
                    
    for key in graph.keys():
        if len(graph[key]) > 0 and key not in temp:
            bfs(key)
    print(result)