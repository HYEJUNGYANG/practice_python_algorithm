import sys
sys.stdin=open("input.txt", "rt")

size = 21
arr = [0] * size
for i in range(size):
    arr[i] = i

for x in range(10):
    ai, bi = map(int, input().split())
    a = list(arr[ai:bi+1])
    a = a[::-1]
    for j in range(ai, bi + 1):
        arr[j] = a[j-ai]

for b in arr:
    if b == 0:
        continue
    print(b, end=' ')
    