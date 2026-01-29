import sys
input = sys.stdin.readline

for a in sorted(sorted(list(set([input().strip() for _ in range(int(input()))]))), key=lambda x:len(x)):
    print(a)