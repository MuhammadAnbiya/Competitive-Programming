import re

name = input("whats your name ? ").strip()
macthes = re.search(r"^(.+), (.+)$", name)

if macthes:
    name = macthes.group(2) + " " + macthes.group(1)

print(f"hello, {name}")