from statistics import mean
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
mathScore = list(map(int, input().split()))
scoreAverage = round(mean(mathScore))

min = 100
result = min
for index, value in enumerate(mathScore):
    v = abs(scoreAverage - value)
    if min > v:
        min = v
        result = index + 1
    elif min == v:
        if value > mathScore[result - 1]:
            result = index + 1

print(scoreAverage, result)


