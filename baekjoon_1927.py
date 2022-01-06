import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            poped = heapq.heappop(q)
            print(poped)
        continue
    
    heapq.heappush(q, num)