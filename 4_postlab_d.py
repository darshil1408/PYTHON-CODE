list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]
freq = {}
for i in list:
    freq[i] = freq.get(i, 0) + 1
print(freq)