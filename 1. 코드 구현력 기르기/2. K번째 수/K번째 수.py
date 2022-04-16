import sys
sys.stdin=open("input.txt", "rt")

t = int(input())

for i in range(1, t+1):
    n, s, e, k = map(int, input().split())
    array = list(map(int, input().split()))

    newArray = array[s-1:e]
    newArray.sort()
    print("#%d %d" %(i, newArray[k-1]))