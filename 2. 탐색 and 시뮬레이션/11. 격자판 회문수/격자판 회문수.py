import sys
sys.stdin=open("input.txt", "r")

# arr = [list(map(int, input().split())) for _ in range(7)]

# cnt = 0
# for i in range(7):
#     for j in range(3):
#         value = j
#         if arr[i][value] == arr[i][value+4]:
#             if arr[i][value+1] == arr[i][value+3]:
#                 cnt += 1
#         if arr[value][i] == arr[value+4][i]:
#             if arr[value+1][i] == arr[value+3][i]:
#                 cnt += 1
# print(cnt)

# 문제에 나온 풀이
# board = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
# for i in range(3):
#     for j in range(7):
#         # 같은 행에서 비교
#         tmp = board[j][i:i+5]
#         if tmp == tmp[::-1]:
#             cnt += 1
#         # 같은 열에서 비교
#         for k in range(2):
#             if board[i+k][j] != board[i+5-k-1][j]:
#                 break
#         else:
#             cnt += 1
        
# print(cnt)

# <회문의 길이가 가변적일 때 코드>
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
len = 5
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+len]
        if tmp == tmp[::-1]:
            cnt += 1
        #tmp = board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안됨
        for k in range(len//2):
            if board[i+k][j] != board[len-k+i-1][j]:
                break
        else:
            cnt+=1
        
print(cnt)