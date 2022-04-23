import sys
# sys.stdin=open("input.txt", "rt")

# n = int(input())
# arr = list(input().split())

# def digit_sum(x):
#     sum = 0
#     for value in x:
#         sum += int(value)
#     return sum

# sumArr = [0] * len(arr)
# for index, value in enumerate(arr):
#     sumArr[index] = digit_sum(value)

# index = sumArr.index(max(sumArr))
# print(arr[index])

# 문제에 나온 풀이

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    # while x>0:
    #     sum += x % 10
    #     x = x // 10
    # return sum

    for i in str(x):
        sum += int(i)
    return sum

max = 0
for x in a:
    tot=digit_sum(x)
    if(tot > max):
        max = tot
        res = x
print(res)