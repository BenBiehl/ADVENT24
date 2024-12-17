lines = open("input.txt", "r").read().split("\n")

rows = len(lines)
columns = len(lines[0])
match_count = 0

for i in range(0, rows):
    for j in range(0, columns):
        if(lines[i][j]) == "X":
            print(0)

print(match_count)