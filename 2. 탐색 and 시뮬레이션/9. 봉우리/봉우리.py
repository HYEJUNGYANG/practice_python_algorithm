import sys
sys.stdin=open("/Users/hyejung/Desktop/HYEJUNG/Practice/Algorithm/python/practice_python_algorithm/2. 탐색 and 시뮬레이션/9. 봉우리/input.txt", "r")

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n+1):
#     if i < n:
#         arr[i].append(0)
#         arr[i].insert(0, 0)
#     else:
#         arr.insert(0, [0] * (n+2))
#         arr.append([0] * (n+2))
# print(arr)

# cnt = 0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         value = arr[i][j]
#         if arr[i][j-1] < value and arr[i][j+1] < value and arr[i-1][j] < value and arr[i+1][j] < value:
#             cnt += 1
# print(cnt)

# 문제에 나온 풀이

# [⬆️, ➡️, ⬇️, ⬅️]
dx=[-1, 0, 1, 0] # 행
dy=[0, 1, 0, -1] # 열
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all() -> 안에 있는 모든 조건이 참일 때 참
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)