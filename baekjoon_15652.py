N, M = map(int, input().split())

s = []

def solve():
    if len(s) == M:
        print(*s)
        return

    for i in range(1, N + 1):
        if len(s) > 0 and i < s[-1]:
            continue
        s.append(i)
        solve()
        s.pop()
        
solve()