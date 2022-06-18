import sys
sys.stdin=open("input.txt", "r")

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[1])

cnt = 1
for i in range(1, n):
    if arr[i][0] >= arr[i-1][1]:
        cnt += 1
    else:
        arr[i][0], arr[i][1] = arr[i-1][0], arr[i-1][1]
print(cnt)