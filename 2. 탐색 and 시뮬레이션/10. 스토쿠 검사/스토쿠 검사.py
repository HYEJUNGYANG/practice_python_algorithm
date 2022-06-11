from operator import countOf
import sys
sys.stdin=open("input.txt", "r")

def check(a):
    for i in range(9):
        # index 0은 사용x 그냥 1~9 숫자 넣기 편하게 하기 위해 10으로 지정
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            # 중복된 숫자가 존재한다면 중복된 숫자 부분에 1이 덮어씌워지므로 합이 9가 될 수 없음
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")