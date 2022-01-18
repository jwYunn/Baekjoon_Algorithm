n = int(input())

tree = {key:[0,0] for key in range(1, n + 1)}
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def solve(in_start, in_end, post_start, post_end):
    
    root = postorder[post_end]
        
    index = inorder.index(root)
    postorder.index(root)
    
    tree[root][0] = 
    
    solve(in_start, index - 1, post_start, post_start + (index - in_start - 1))
    solve(index + 1, in_end, )
    
    return

def preorder(node):
    
    
    return





solve(0, len(inorder) - 1, 0, len(postorder))
preorder(postorder[-1])
