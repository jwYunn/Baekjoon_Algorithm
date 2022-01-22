N = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array)

while start <= end:
    mid = (start + end) // 2
    count = 0
    temp = 0
    
    for i in array:
        if not temp:
            temp = i
            continue
        if temp < i:
            count += 1
    
    
        
    
    