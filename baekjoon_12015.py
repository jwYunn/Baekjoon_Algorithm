import sys 
input = sys.stdin.readline 
n = int(input()) 
array = list(map(int, input().split())) 
lis = [0] 


for num in array:
    if lis[-1] < num: 
        lis.append(num) 
    else: 
        left = 0 
        right = len(lis) 
        
        while left < right: 
            mid = (right + left) // 2 
            if lis[mid] < num: 
                left = mid + 1 
            else: 
                right = mid 
        lis[right] = num 
        
print(len(lis)-1)
