N = int(input())

s = [0] * (N + 1)
s[1] = 9

for i in range(2, N + 1):
    one_count = 2 ** (i - 2)
    s[i] = (s[i - 1] - one_count) * 2 + one_count * 1
    
print(s[N])