m = list(input())
n = list(input())
m_len = len(m)
n_len = len(n)

dp = [[0] * (n_len + 1) for i in range(m_len + 1)]

