from statistics import mean
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
mathScore = list(map(int, input().split()))
scoreAverage = round(mean(mathScore))

min = 100
result = min
for index, score in enumerate(mathScore):
    v = abs(scoreAverage - score)
    if min > v:
        min = v
        result = index + 1
    elif min == v:
        if score > mathScore[result - 1]:
            result = index + 1

print(scoreAverage, result)


