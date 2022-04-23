import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

# primeArr = [1] * (n+1)

# for i in range(2, n+1):
#     if primeArr[i]:
#         for j in range(i*i, n+1, i):
#             primeArr[j] = 0  # not primeNum

# cnt = -2
# for x in primeArr:
#     if x:
#         cnt += 1
# print(cnt)

# 문제에 나온 풀이

ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)