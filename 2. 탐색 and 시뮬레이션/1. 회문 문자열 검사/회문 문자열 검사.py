from pickle import TRUE
import sys

from numpy import true_divide
sys.stdin=open("input.txt", "rt")

n = int(input())

for i in range(n):
    string = input()
    string = string.lower()
    size = len(string)
    isSame = "YES"   
    for x in range(size//2):
        if string[x] == string[-(x+1)]:
            isSame = "YES"
        else:
            isSame = "NO"
            break
    print("#", i+1, " ", isSame, sep='')