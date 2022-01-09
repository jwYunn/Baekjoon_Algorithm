import sys
input = sys.stdin.readline

def bfs(start_node):
    visited, need_visited = [], []
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            temp.append(node)
            need_visited.extend(graph[node])
    result.append(len(visited))
    return

N = int(input())
array = []
graph = {key:[] for key in range(N * N)}
temp = []
result = []

for _ in range(N):
    row = input().strip()
    array.append(row)
    
index = 0

for i in range(N):
    for j in range(N):
        nothing = False
        
        if array[i][j] == '1':
            if i > 0 and array[i - 1][j] == '1':
                graph[index].append(index - N)
                nothing = True
        
            if i < N - 1 and array[i + 1][j] == '1':
                graph[index].append(index + N)
                nothing = True
                
        
            if j > 0 and array[i][j - 1] == '1':
                graph[index].append(index - 1)
                nothing = True
                
        
            if j < N - 1 and array[i][j + 1] == '1':
                graph[index].append(index + 1)
                nothing = True
            
            if not nothing:
                result.append(1)   
        index += 1
        

for key in graph.keys():
    if len(graph[key]) > 0 and key not in temp:
        bfs(key)
        
result = sorted(result)
print(len(result))
for value in result:
    print(value)