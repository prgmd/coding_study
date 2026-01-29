# 여기에 코드를 입력해주세요
import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()


for num in numbers:
    print(num)