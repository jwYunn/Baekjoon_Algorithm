n, m = map(int, input().split())

s = []

def solve():
    if len(s) == m:
        print(*s)
        
    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        solve()
        s.pop()
    
solve()