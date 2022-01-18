import sys
input = sys.stdin.readline

preorder = []
count = 0

while count <= 10000:
    try:
        node = int(input())
    except:
        break
    preorder.append(node)
    
    count += 1
    
    

root = preorder[0]
tree = {key:[0, 0] for key in range(1, 1000000 + 1)}

for i in range(len(preorder) - 1):
    if preorder[i] > preorder[i + 1]:
        tree[preorder[i]][0] = preorder[i + 1]
        # print(preorder[i] ," :", tree[preorder[i]])
    else:
        for j in range(i, -1, -1):
            if preorder[j] > preorder[i + 1]:
                tree[preorder[j + 1]][1] = preorder[i + 1]
                # print(preorder[j + 1], ":", tree[preorder[j + 1]])
                break
            if j == 0:
                tree[preorder[j]][1] = preorder[i + 1]
                # print(preorder[j], ":", tree[preorder[j + 1]])
# print(tree)

def postorder(root_node):
    if root_node != 0:
        postorder(tree[root_node][0])
        postorder(tree[root_node][1])
        print(root_node)
    
#     return

postorder(root)