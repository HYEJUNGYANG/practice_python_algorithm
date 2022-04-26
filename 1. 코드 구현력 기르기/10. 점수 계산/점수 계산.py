import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
score = list(map(int, input().split()))

cnt = 0
result = 0
for i in score:
    if i == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0
print(result)