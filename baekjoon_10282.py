import heapq
from re import I
import sys
input = sys.stdin.readline

def dijkstra(start):
    
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    
    while q:
        current_distance, current_node = heapq.heappop(q)
        
        if distances[current_node] < current_distance:
            continue
        
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(q, [distance, adjacent])
                
    return distances

test_case = int(input())

for _ in range(test_case):
    n, d, c = map(int, input().split())
    graph = {key : {} for key in range(1, n + 1)}
    distances = {key : float('inf') for key in range(1, n + 1)}
    
    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b][a] = s
        
    dijkstra(c)
    
    count = 0
    max_distance = 0
    for key, value in distances.items():
        if value == float('inf'):
            continue
        count += 1
        if value > max_distance:
            max_distance = value
    print(count, max_distance)