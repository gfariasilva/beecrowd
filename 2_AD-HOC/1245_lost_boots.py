import sys

for line in sys.stdin:
    boots = {}
    result = 0
    for i in range(int(line.strip())):
        size, foot = input().strip().split()

        if size in boots.keys():
            boots[size].append(foot)
        else:
            boots[size] = [foot]

    for item in boots.items():
        left = item[1].count('E')
        right = item[1].count('D')

        result += min([left, right])

    print(result)