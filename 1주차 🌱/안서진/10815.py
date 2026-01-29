import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

for card in check:
    if card in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
