import sys
input = sys.stdin.readline

array = []
answer1 = 0
answer2 = 0
answer3 = 0
    
def scan(n, row, col):
    
    isSame = False
    haveMinus = False
    haveZero = False
    haveOne = False
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            if array[i][j] == -1:
                haveMinus = True
            if array[i][j] == 0:
                haveZero = True
            if array[i][j] == 1:
                haveOne = True
                
    if (haveMinus and not haveZero and not haveOne) or (haveZero and not haveMinus and not haveOne) or (haveOne and not haveZero and not haveMinus):
        isSame = True            
    
    if isSame:
        return True, array[row][col]
    else:
        return False, -2


def solve(n, row, col):
    global answer1
    global answer2
    global answer3
    
    isSame, result = scan(n, row, col)
    
    if isSame:
        if result == -1:
            answer1 += 1
        elif result == 0:
            answer2 += 1
        else:
            answer3 += 1
    else:
        n //= 3
        solve(n, row + n * 0, col + n * 0)        
        solve(n, row + n * 0, col + n * 1)        
        solve(n, row + n * 0, col + n * 2)        

        solve(n, row + n * 1, col + n * 0)        
        solve(n, row + n * 1, col + n * 1)        
        solve(n, row + n * 1, col + n * 2)        

        solve(n, row + n * 2, col + n * 0)        
        solve(n, row + n * 2, col + n * 1)        
        solve(n, row + n * 2, col + n * 2)        

if __name__ == "__main__":
    
    N = int(input())
   
    
    for _ in range(N):
        val = list(map(int, input().split()))
        array.append(val)
        
    solve(N, 0, 0)
    print(answer1)
    print(answer2)
    print(answer3)