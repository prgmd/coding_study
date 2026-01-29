from collections import defaultdict
import sys
input = sys.stdin.readline

d = defaultdict(int)
for _ in range(int(input())):
    d[int(input())] += 1

num_list = sorted(d.keys())
for n in num_list:
    for _ in range(d[n]):
        print(n)