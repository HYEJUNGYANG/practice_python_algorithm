import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

# for i in range(n):
#     string = input()
#     string = string.lower()
#     size = len(string)
#     for x in range(size//2):
#         if string[x] != string[-(x+1)]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

# 다른 풀이

for i in range(n):
    s = input()
    s = s.lower()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))