import sys
input = sys.stdin.readline

K, N = map(int, input().split())
array = []

for _ in range(K):
    lan = int(input())
    array.append(lan)
    
start, end = 1, max(array)
mid = 0


while start <= end:
    mid = (start + end) // 2
    line = 0
    
    for i in array:
        line += i // mid
        
    if line >= N:
        start = mid + 1
    else:
        end = mid - 1 
        
print(end)