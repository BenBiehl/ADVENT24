lines = open("input.txt", "r").read().split("\n")

left = []
right = []
total_similarity= 0

for line in lines:
    x = line.split()
    left.append(int(x[0]))
    right.append(int(x[1]))

for num in left:
    total_similarity += num * right.count(num)

print(total_similarity)