import sys

for line in sys.stdin:
    n = int(line.strip())
    start = input().strip().split()
    finish = input().strip().split()
    overtakes = 0
    finish_pos = {car: idx for idx, car in enumerate(finish)}
    threshold = 0
    
    while start != finish:
        for current_pos, car in enumerate(start):
            final_pos = finish_pos[car]
            if max(0, current_pos - final_pos) > 0:
                start.remove(car)
                start.insert(final_pos, car)
            overtakes += max(0, current_pos - final_pos)
    
    print(overtakes)