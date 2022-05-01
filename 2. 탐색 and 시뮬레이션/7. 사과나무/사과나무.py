import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

sum = 0
half = n//2
for i in range(n):
    if i == half:
        sum += arr[half][i]
        continue
    sum = sum + arr[half][i] + arr[i][half]

num = 3
for i in range(n//2 - 1):
    start = (n-num) // 2
    for j in range(start, start+num):
        if j == half:
            continue
        sum += arr[i+1][j]
        sum += arr[n-i-2][j]
    num += 2
print(sum)