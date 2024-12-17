def is_safe(report):
    n = len(report)
    is_increasing = all(0 < report[i + 1] - report[i] <= 3 for i in range(n - 1))
    is_decreasing = all(0 < report[i] - report[i + 1] <= 3 for i in range(n - 1))
    return is_increasing or is_decreasing

lines = open("input.txt", "r").read().splitlines()

safe_num = 0

for line in lines:
    if not line.strip():
        continue

    report = list(map(int, line.split()))

    if is_safe(report):
        safe_num += 1
        continue

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            safe_num += 1
            break

print(safe_num)
