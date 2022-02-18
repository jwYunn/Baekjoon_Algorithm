import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    V, E = map(int, input().split())
    
    for __ in range(E):
        u, v = map(int, input().split())
        
        