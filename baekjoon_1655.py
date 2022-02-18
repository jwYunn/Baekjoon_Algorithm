import sys
import heapq

input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []
result = []

for i in range(N):
    num = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))
    
    if right_heap and left_heap[0][1] > right_heap[0][0]:
        min = heapq.heappop(right_heap)[0]
        max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min, min))
        heapq.heappush(right_heap, (max, max))
        
    result.append(left_heap[0][1])
    
for j in result:
    print(j)