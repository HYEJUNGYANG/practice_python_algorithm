import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

arr = nArr + mArr
arr.sort()

for x in arr:
    print(x, end=' ')