import sys
sys.stdin=open("input.txt", "r")

# n, c = map(int, input().split())
# stables = []

# for _ in range(n):
#     temp = int(input())
#     stables.append(temp)

# stables.sort()

# left = 1
# right = stables[-1]

# res = 0
# while left <= right:
#     mid = (left + right) // 2
#     p = stables[0]
#     cnt = 0
#     for i in range(1, n):
#         if stables[i] - p < mid:
#             cnt += 1
#         else:
#             p = stables[i]
#     if (n-cnt) >= c:
#         res = mid
#         left = mid + 1
#     else:
#         right = mid - 1
# print(res)

# 문제에 나온 풀이
def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        # 나랑 반대로 이렇게 하면 헷갈리지 않게 cnt값 바로 이용하여 풀 수 있음
        # 나는 (n - cnt)해야 해서 자칫하고 빼먹거나 하면 예상치 못한 결과 나올 수 있음
        if Line[i]-ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1
rt = Line[n-1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
