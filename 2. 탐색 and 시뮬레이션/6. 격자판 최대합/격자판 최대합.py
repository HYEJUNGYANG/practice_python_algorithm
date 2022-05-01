import sys
sys.stdin=open("input.txt", "rt")

# n = int(input())
# arr = []

# for i in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)

# max = 0
# for i in range(n):
#     sumRow = 0
#     sumCol = 0
#     sumLDiag = 0
#     sumRDiag = 0
#     for j in range(n):
#         sumRow += arr[i][j]
#         sumCol += arr[j][i]
#         sumLDiag += arr[j][j]
#         sumRDiag += arr[i][n-j-1]
#     if sumRow > max:
#         max = sumRow
#     if sumCol > max:
#         max = sumCol
#     if sumLDiag > max:
#         max = sumLDiag
#     if sumRDiag > max:
#         max = sumRDiag
# print(max)

# 문제에 나온 풀이

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = 0
for i in range(n):
    sum1 = sum2 = 0  # sum1 => 행의 합, sum2 => 열의 합
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0 # 대각선 합 구하기 위해 초기화
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)