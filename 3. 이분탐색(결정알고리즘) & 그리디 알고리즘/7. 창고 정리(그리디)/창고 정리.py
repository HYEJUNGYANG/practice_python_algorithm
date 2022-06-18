import sys
sys.stdin=open("input.txt", "r")

l = int(input())
height = list(map(int, input().split()))
m = int(input())
height.sort()

for _ in range(m):
    height[0] += 1
    height[-1] -= 1
    height.sort()
print(height[-1] - height[0])