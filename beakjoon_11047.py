import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = []
result = 0

for _ in range(N):
    coin = int(input())
    
    if coin <= K:
        coin_list.append(coin)
    
for i in range(len(coin_list)):
    poped = coin_list.pop()
    if K - poped >= 0:
        result += K // poped
        K -= K // poped * poped
        
print(result)