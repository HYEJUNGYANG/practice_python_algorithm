import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            arr[h-1].append(arr[h-1].pop(0))
    else:
        for _ in range(k):
            arr[h-1].insert(0, arr[h-1].pop())

res = 0
start = 0
end = n-1
for i in range(n):
    for j in range(start, end+1):
        res += arr[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(res)