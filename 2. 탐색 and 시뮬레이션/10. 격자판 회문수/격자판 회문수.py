import sys
sys.stdin=open("input.txt", "r")

a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        temp = a[i][j:j+5]
        tmp = list(a[k][i] for k in range(j, j+5))
        if temp == temp[::-1]:
            cnt += 1
        elif tmp == tmp[::-1]:
            cnt += 1
print(cnt)