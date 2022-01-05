exp = input()

temp = 0
isFirst = True
new_exp = ""
b = ""
for i in range(len(exp)):
    if exp[i] == '+' or exp[i] == '-':
        num = int(exp[temp:i])
        new_exp += str(num)
        new_exp += exp[i]
        temp = i + 1
    
    if i == len(exp) - 1:
        num = int(exp[temp:])
        new_exp += str(num)
        
for i in new_exp:
    if i == '-':
        if isFirst:
            b += i + '('
            isFirst = False
        else:
            b += ')' + i + '('
            isFirst = True
    else:
        b += i


if isFirst:
    b += ')'
        
print(b)
result = eval(b)

print(result)    