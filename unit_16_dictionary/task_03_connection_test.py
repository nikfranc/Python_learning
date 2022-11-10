data = str(input()).split()
counts = {}
for word in data:
    counts[word] = counts.get(word, 0) + 1
    print(counts[word], end=' ')