from statistics import mean
import sys
sys.stdin=open("input.txt", "rt")

# n = int(input())
# mathScore = list(map(int, input().split()))
# scoreAverage = round(mean(mathScore))

# min = 100
# result = min
# for index, score in enumerate(mathScore):
#     v = abs(scoreAverage - score)
#     if min > v:
#         min = v
#         result = index + 1
#     elif min == v:
#         if score > mathScore[result - 1]:
#             result = index + 1

# print(scoreAverage, result)


# 문제에 나온 풀이
'''
round()는 round_half_even 방식임!
4.5와 같이 정확하게 반이면 짝수쪽에 가까운 값으로 -> 4로 바뀜
5.5 -> 6
4.511 -> 5
'''

n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/n + 0.5)
min = 100
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
