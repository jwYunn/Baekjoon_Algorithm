import sys
input = sys.stdin.readline

array = []
blank_list = []

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 0:
            blank_list.append((i, j))
    array.append(row)
    
def check(row, col):
    num = [1,2,3,4,5,6,7,8,9]

    # row 조건
    for i in array[row]:
        if i in num:
            num.remove(i)           
    
    # col 조건
    for i in range(9):
        if array[i][col] in num:
            num.remove(array[i][col])
    
    # 정사각형 조건
    x = row // 3
    y = col // 3
    
    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            if array[i][j] in num:
                num.remove(array[i][j])    
    
    return num

def solve(idx):

    row, col = blank_list[idx]
    can = check(row, col)
    
    if len(can) == 0:
        return False
    
    if idx == len(blank_list) - 1:
        array[row][col] = can[0]
        print_sdoku()
        exit(0)
    
    for i in can:
        array[row][col] = i
        for j in range(idx + 1, len(blank_list)):
            
            if not solve(j):
                array[row][col] = 0
                break
    if array[row][col] == 0:
        return False        
    return True

def print_sdoku():
    for i in range(9):
        for j in range(9):
            print(array[i][j], end=' ')
        print()

solve(0)