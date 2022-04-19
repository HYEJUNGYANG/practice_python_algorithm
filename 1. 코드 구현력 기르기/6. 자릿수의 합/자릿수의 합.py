import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(input().split())

def digit_sum(x):
    sum = 0
    for value in x:
        sum += int(value)
    return sum

sumArr = [0] * len(arr)
for index, value in enumerate(arr):
    sumArr[index] = digit_sum(value)

index = sumArr.index(max(sumArr))
print(arr[index])