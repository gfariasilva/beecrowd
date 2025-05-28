while True:
    h1, m1, h2, m2 = map(int,  input().strip().split())

    if not m1 and not m2 and not h1 and not h2:
        break

    hour1 = h1*60
    time1 = hour1 + m1

    hour2 = h2*60
    time2 = hour2 + m2

    if time2 < time1:
        time2 += 60*24
    
    print(time2 - time1)