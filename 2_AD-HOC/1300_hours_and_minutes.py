import sys

angles = [0]

minutes = 0
hours = 0
for i in range(1, 121):
    minutes += 1
    if not i % 12:
        hours += 1

    angles.append(abs(minutes - hours) * 6)

for line in sys.stdin:
    angle = int(line.strip())
    print('Y' if angle in angles else 'N')