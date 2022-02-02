import sys
input = sys.stdin.readline

array = []
answer = ""

def scan(n, row, col):
    haveZero = False
    haveOne = False
    result = 0
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            if array[i][j] == 1:
                haveOne = True
            else:
                haveZero = True
            if haveZero and haveOne:
                return False
    if haveOne:
        result = 1
    else:
        result = 0        

    return True, result

def solve(n, row, col):
    global answer
    
    isSame, result = scan(n, row, col)  

    if isSame:
        answer += result
    else:
        n //= 2
        solve(n, row, col)        
        solve(n, row, col + n)        
        solve(n, row + n, col)        
        solve(n, row + n, col + n)        

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        val = list(map(str, input().split()))
        array.append(val)
    
    solve(N)
    print(array)