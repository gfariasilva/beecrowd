import sys

for line in sys.stdin:
    for case in range(int(line.strip())):
        shots = int(input())
        heights = map(int, input().strip().split())
        patterns = list(input().strip())
        hits = 0

        for i, height in enumerate(heights):
            if (patterns[i] == 'J' and height > 2) or (patterns[i] == 'S' and height < 3):
                hits += 1
        
        print(hits)