original = [2, 8, 9, 48, 8, 22, -12, 2]
print(original)
filtered = [original[i] + 2 for i in range(len(original)) if original[i] > 5]
print(filtered)