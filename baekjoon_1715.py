import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
result = 0

for _ in range(N):
    num = int(input())
    heapq.heappush(q, num)
    
while len(q) != 1:
    one = heapq.heappop(q) 
    two = heapq.heappop(q) 
    one_value = one + two
    result += one_value
    heapq.heappush(q, one_value)    
    
print(result)