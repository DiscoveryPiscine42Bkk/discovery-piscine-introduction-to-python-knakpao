original = [2, 8, 9, 48, 8, 22, -12, 2]
output = []
seen = set()

for num in original:
    if num > 5 and num not in seen:
        output.append(num + 16)
        seen.add(num)
print(output)