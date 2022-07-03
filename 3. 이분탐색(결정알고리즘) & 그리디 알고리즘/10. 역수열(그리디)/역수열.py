import sys
sys.stdin=open("input.txt", "r")

n = int(input())
sequence = list(map(int, input().split()))

a = [0] * n
for i in range(n):
    for j in range(n):
        # sequence[i] == 0이면 자기 앞에 큰 숫자들의 빈공간을 다 만들었다는 의미
        # a[j] == 0 이면 빈자리 이므로 자리를 찾아가는 것
        if sequence[i] == 0 and a[j] == 0:
            a[j] = i + 1
            break;
        # 아직 자리를 찾지 못했다면
        elif a[j] == 0:
            sequence[i] -= 1
for x in a:
    print(x, end=' ')