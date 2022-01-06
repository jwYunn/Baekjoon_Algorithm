import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []


for _ in range(N):
    num = int(input())
    heapq.heappush(q, -num)
    
    if num == 0:
        poped = heapq.heappop(q)
        print(-poped)