import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def recursive(x, y, N):
    global white
    global blue
    
    val = array[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if val != array[i][j]:
                recursive(x, y, N // 2)
                recursive(x, y+N//2, N // 2)
                recursive(x+N//2, y, N // 2)
                recursive(x+N//2, y+N//2, N // 2)
                return
    if val == 0:
        white += 1
    else:
        blue += 1

recursive(0, 0, N)
print(white)
print(blue)