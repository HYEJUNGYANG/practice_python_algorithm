import sys
sys.stdin=open("input.txt", "rt")

# n, m = map(int, input().split())
# if n > m:
#     min = m + 1
#     max = n + 1
# elif n < m:
#     min = n + 1
#     max = m + 1
# else:
#     min = n
#     max = m
#     result = n + 1

# if (min != max):
#     for i in range(min, max+1):
#         print(i, end=' ')
# else:
#     print(result)

# 문제에서 나온 풀이
n, m = map(int, input().split())
cnt= [0] * (n + m + 1)
max = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
        
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')