import sys
sys.stdin=open("input.txt", "r")

n, c = map(int, input().split())
stables = []

for _ in range(n):
    temp = int(input())
    stables.append(temp)

stables.sort()

left = 1
right = stables[-1]

res = 0
while left <= right:
    mid = (left + right) // 2
    p = stables[0]
    cnt = 0
    for i in range(1, n):
        if stables[i] - p < mid:
            cnt += 1
        else:
            p = stables[i]
    if (n-cnt) >= c:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)