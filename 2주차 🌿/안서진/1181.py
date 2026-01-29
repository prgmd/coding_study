# 단어 정렬 (실버5)

N = int(input())

words = []
for word in range(N):
    words.append(input())

words = set(words)
words = list(words)

words.sort(key=lambda x: (len(x),x))

print(*words, sep = '\n')