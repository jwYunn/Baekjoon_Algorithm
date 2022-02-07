from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def solve(start, end):
    global post_order
    if end - start < 0:
        return
    
    if end - start == 0:
        post_order.append(pre_order[start])
        return
    
    root = pre_order[start]
    post_order.append(root)
    
    standard = -1
    
    for i in range(start + 1, end + 1):
        if root < pre_order[i]:
            standard = i   
            break
            
    if standard != -1: 
        left_start = start + 1
        left_end = standard - 1
        
        right_start = standard
        right_end = end
        
        solve(right_start, right_end)
        solve(left_start, left_end)

    else:
        solve(start + 1, end)

if __name__ == "__main__":

    pre_order = []
    post_order = deque()
    
    while True:
        try:
            value = int(input())
            pre_order.append(value)
        except:
            break
            
    solve(0, len(pre_order) - 1)
    
    while post_order:
        print(post_order.pop())