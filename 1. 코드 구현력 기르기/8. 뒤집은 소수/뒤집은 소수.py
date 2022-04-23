import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    rev = 0
    while x > 0:
        rev = (rev * 10) + (x % 10)
        x = x // 10
    return rev

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for a in arr:
    a = reverse(a)
    if isPrime(a):
        print(a, end=' ')
