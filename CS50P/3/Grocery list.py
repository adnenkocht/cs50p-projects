from collections import Counter
items = []
print("Enter items (type 'ctrl Z' to finish):")
while True:
    try:
        item = input("Item: ").strip().title()
        items.append(item)
    except EOFError:
        break
counts = Counter(items)
for item in sorted(counts):
    print(f"{item}: {counts[item]}")