import re

email = input("whats is your email ? ").strip()

if re.search(".?@", email):
    print("valid")
else:
    print("invalid")