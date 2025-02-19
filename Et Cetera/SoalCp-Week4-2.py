def is_valid_name(name):
    return len(name) > 4 and name[0].lower() in "aeiou"

n = int(input("Enter the number of cat names: "))

cat_names = [input().strip() for _ in range(n)]

valid_names = []
for name in cat_names:
    if is_valid_name(name) and name not in valid_names:
        valid_names.append(name)

if valid_names:
    print("\n".join(valid_names))
else:
    print("No valid names found.")
