import sys
input = sys.stdin.readline

N = int(input())
array = []
s = []
answer = sys.maxsize
idx = 0
case = []

for _ in range(N):
    row = list(map(int, input().split()))
    array.append(row)

def calc(s):
    rest = [i for i in range(1, N  + 1)]
    team1_val = 0
    team2_val = 0
        
    for i in range(len(s) - 1):
        rest.remove(s[i])
        for j in range(i + 1, len(s)):
            team1_val += array[s[i] - 1][s[j] - 1]
            team1_val += array[s[j] - 1][s[i] - 1]
                
    rest.remove(s[-1])
        
    for i in range(len(rest) - 1):
        for j in range(i + 1, len(rest)):
            team2_val += array[rest[i] - 1][rest[j] - 1]
            team2_val += array[rest[j] - 1][rest[i] - 1]
            
    return team1_val, team2_val

def check(v1, v2):
    global answer
    if abs(v1 - v2) < answer:
        answer = abs(v1 - v2)
    
def solve(index):
    
    if len(s) == N // 2:
        case.append(set(s))
        v1, v2 = calc(s)
        check(v1, v2)
        return
    
    for i in range(index, N):
        if i in s:
            continue
        s.append(i)
        solve(i + 1)
        s.pop()


if __name__ == "__main__":
    solve(0)
    print(answer)