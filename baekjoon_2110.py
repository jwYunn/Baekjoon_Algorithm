import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = []

for _ in range(N):
    num = int(input())
    array.append(num)
    
array = sorted(array)

start = 1
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)