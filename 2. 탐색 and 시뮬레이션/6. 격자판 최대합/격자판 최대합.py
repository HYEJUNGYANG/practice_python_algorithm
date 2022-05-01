import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

max = 0
for i in range(n):
    sumRow = 0
    sumCol = 0
    sumLDiag = 0
    sumRDiag = 0
    for j in range(n):
        sumRow += arr[i][j]
        sumCol += arr[j][i]
        sumLDiag += arr[j][j]
        sumRDiag += arr[n-j-1][n-j-1]
    if sumRow > max:
        max = sumRow
    elif sumCol > max:
        max = sumCol
    elif sumLDiag > max:
        max = sumLDiag
    elif sumRDiag > max:
        max = sumRDiag
print(max)