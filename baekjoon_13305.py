N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

temp = cost[0]
result = 0

for i in range(len(cost) - 1):
    result += temp * distance[i]
    if temp >= cost[i + 1]:
        temp = cost[i + 1]
        
print(result)