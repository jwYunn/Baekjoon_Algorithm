N, M = map(int, input().split())

s = []

def solve():
    if len(s) == M:
        print(*s)
        return
    
    for i in range(1, N + 1):
        if i in s:
            continue
        if len(s) > 0 and s[-1] > i:
            continue
        s.append(i)
        solve()
        s.pop()
        
solve()