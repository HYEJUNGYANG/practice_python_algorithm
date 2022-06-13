import sys
sys.stdin=open("input.txt", "r")

def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt

k, n = map(int, input().split())
Line = [] # k개의 랜선을 받아들이기 위함
res = 0
largest = 0
# for문으로 k개의 랜선을 Line에 넣어줌
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp) # 가장 긴 랜선의 길이를 찾아 범위를 지정하기 위해
# 초기 이분검색 범위 1 ~ largest (cm)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)