# 숫자 카드 2 (실4)
from collections import defaultdict

N = int(input())
# 가지고 있는 숫자 카드들 
cards = list(map(int, input().split()))
N_cards = defaultdict(int)

for card in cards:
    N_cards[card] += 1

M = int(input())
number_B = list(map(int, input().split()))

ans = []
for num in number_B :
    ans.append(N_cards[num])

print(*ans)