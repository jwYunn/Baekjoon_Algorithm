import sys
sys.setrecursionlimit(10**5)

def solve(in_start, in_end, post_start, post_end):
    global pre_order

    if in_end - in_start < 0:
        return
    
    if in_end - in_start == 0:
        pre_order.append(in_order[in_start])
        return
    
    # find in_order root index
    root = post_order[post_end]
    
    pre_order.append(root)
        
    in_order_root_index = -1
    for i in range(in_start, in_end + 1):
        if root == in_order[i]:
            in_order_root_index = i
            break
    
    in_left_start = in_start
    in_left_end = in_order_root_index - 1 

    in_right_start = in_order_root_index + 1
    in_right_end = in_end

    post_left_start = post_start      
    post_left_end = post_start + (in_left_end - in_left_start)

    post_right_start = post_left_end + 1
    post_right_end = post_right_start + (in_right_end - in_right_start)
    
    solve(in_left_start, in_left_end, post_left_start, post_left_end)
    solve(in_right_start, in_right_end, post_right_start, post_right_end)

    
if __name__ == "__main__":
    n = int(input())
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    pre_order = []
    solve(0, len(in_order) - 1, 0, len(post_order) - 1)
    print(*pre_order)