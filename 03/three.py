import re

string = open("input.txt", "r").read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
total = 0
mul_enabled = True
matches = re.finditer(pattern, string)

for match in matches:
    if match.group(0) == "do()":
        mul_enabled = True
    elif match.group(0) == "don't()":
        mul_enabled = False
    elif match.group(1) and match.group(2):
        if mul_enabled:
            x = int(match.group(1))
            y = int(match.group(2))
            total += x * y

print(total)
