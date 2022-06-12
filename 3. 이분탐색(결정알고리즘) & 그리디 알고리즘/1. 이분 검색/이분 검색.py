import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

left = 0
right = n-1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == m:
        print(mid + 1)
        break;
    elif a[mid] > m:
        right = mid - 1
    else:
        left = mid + 1
