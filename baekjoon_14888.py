import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def check(num):
    global max_val
    global min_val
    
    if num > max_val:
        max_val = num
    
    if num < min_val:
        min_val = num

def solve(index, num, add, sub, mul, div):
    
    if index == len(num_list) - 1:
        check(num)
        return
    
    if add > 0:
        solve(index + 1, num + num_list[index + 1], add - 1, sub, mul, div)
    if sub > 0:
        solve(index + 1, num - num_list[index + 1], add, sub - 1, mul, div)
    if mul > 0:
        solve(index + 1, num * num_list[index + 1], add, sub, mul - 1, div)
    if div > 0:
        solve(index + 1, int(num / num_list[index + 1]), add, sub, mul, div - 1)

solve(0, num_list[0], plus, minus, mul, div)
print(max_val)
print(min_val)