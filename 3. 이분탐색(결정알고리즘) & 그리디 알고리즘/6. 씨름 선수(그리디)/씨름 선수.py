import sys
sys.stdin=open("input.txt", "r")

n = int(input())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))
info.sort(reverse=True)

max_weight = 0
cnt = 0
for h, w in info:
    if w > max_weight:
        cnt += 1
        max_weight = w
print(cnt)