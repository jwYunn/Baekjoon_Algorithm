N = int(input())
array = list(map(int, input().split()))

max_val = max(array)
count = array.count(max_val)
result = []
index = 0
index_list = []

increase = [1] * N
decrease = [1] * N

for i in range(N):
    if array[i] == max_val:
        index_list.append(i)
    for j in range(i):
        if array[i] > array[j]:
            increase[i] = max(increase[i], increase[j] + 1)
    

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if array[i] > array[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
            
for i in range(N):
    value = increase[i] + decrease[i] - 1
    result.append(value)

print(max(result)) 