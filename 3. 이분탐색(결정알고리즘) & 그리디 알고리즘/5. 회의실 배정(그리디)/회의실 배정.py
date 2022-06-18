import sys
sys.stdin=open("input.txt", "r")

# n = int(input())

# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
# arr.sort(key=lambda x:x[1])

# cnt = 1
# for i in range(1, n):
#     if arr[i][0] >= arr[i-1][1]:
#         cnt += 1
#     else:
#         arr[i][0], arr[i][1] = arr[i-1][0], arr[i-1][1]
# print(cnt)


# 문제에 있는 풀이
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # 튜플 형태로 저장
# x[1]을 우선으로 정렬하고 같을 때 x[0] 비교
# 그냥 sort() 하면 x[0]을 우선으로 정렬
meeting.sort(key=lambda x : (x[1], x[0]))
end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)