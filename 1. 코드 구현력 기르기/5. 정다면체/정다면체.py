import sys
sys.stdin=open("input.txt", "rt")

n, m = map(int, input().split())
if n > m:
    min = m + 1
    max = n + 1
elif n < m:
    min = n + 1
    max = m + 1
else:
    min = n
    max = m
    result = n + 1

if (min != max):
    for i in range(min, max+1):
        print(i, end=' ')
else:
    print(result)