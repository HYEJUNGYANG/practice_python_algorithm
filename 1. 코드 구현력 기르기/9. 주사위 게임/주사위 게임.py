import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

max = 0
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] == arr[1] == arr[2]:
        price = 10000 + arr[1] * 1000
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        price = 1000 + arr[1] * 100
    else:
        price = arr[2] * 100
    if max < price:
        max = price
print(max)