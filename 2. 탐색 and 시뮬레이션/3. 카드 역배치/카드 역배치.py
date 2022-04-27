import sys
sys.stdin=open("input.txt", "rt")

# size = 21
# arr = [0] * size
# for i in range(size):
#     arr[i] = i

# for x in range(10):
#     ai, bi = map(int, input().split())
#     a = list(arr[ai:bi+1])
#     a = a[::-1]
#     for j in range(ai, bi + 1):
#         arr[j] = a[j-ai]

# for b in arr:
#     if b == 0:
#         continue
#     print(b, end=' ')


# 문제에 나온 풀이!
# a, b = b, a -> 파이썬에서의 swap
a = list(range(21))
for _ in range(10):  # _로 작성하면 변수가 없이 반복
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')