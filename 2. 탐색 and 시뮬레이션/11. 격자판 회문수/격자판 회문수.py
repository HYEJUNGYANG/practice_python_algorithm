import sys
sys.stdin=open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        value = j
        if arr[i][value] == arr[i][value+4]:
            if arr[i][value+1] == arr[i][value+3]:
                cnt += 1
        if arr[value][i] == arr[value+4][i]:
            if arr[value+1][i] == arr[value+3][i]:
                cnt += 1
print(cnt)
