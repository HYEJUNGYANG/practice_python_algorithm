from array import array
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# sum = 0
# half = n//2
# for i in range(n):
#     if i == half:
#         sum += arr[half][i]
#         continue
#     sum = sum + arr[half][i] + arr[i][half]

# num = 3
# for i in range(n//2 - 1):
#     start = (n-num) // 2
#     for j in range(start, start+num):
#         if j == half:
#             continue
#         sum += arr[i+1][j]
#         sum += arr[n-i-2][j]
#     num += 2
# print(sum)

# 문제에 나온 풀이

res = 0
start = end = n//2
for i in range(n):
    for j in range(start, end+1):
        res += arr[i][j]
    if i < n//2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1
print(res)