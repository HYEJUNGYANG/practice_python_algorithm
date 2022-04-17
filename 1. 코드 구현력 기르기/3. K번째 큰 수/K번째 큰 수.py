import sys
sys.stdin=open("input.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            sum.add(arr[i]+arr[j]+arr[m])
sum = list(sum)
sum.sort(reverse=True)

print(sum[k-1])