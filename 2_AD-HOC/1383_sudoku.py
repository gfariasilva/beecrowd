original = list(range(1,10))

for i in range(int(input())):
    matrix = {
        'rows': [],
        'columns': [[],[],[],[],[],[],[],[],[]],
        'sub':[]
    }

    valid = True

    for _ in range(9):
        row = list(map(int, input().strip().split()))
        if sorted(row) != original:
            valid = False
            break
        sliced_row = [row[:3], row[3:6], row[6:9]]
        matrix['rows'].append(row)
        [matrix['columns'][i].append(number) for i, number in enumerate(row)]

    print(f'Instancia {i+1}')
    if not valid:
        print('NAO\n')
        continue

    for box_row in range(0,9,3):
        for box_column in range(0,9,3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(matrix['rows'][box_row + i][box_column + j])
                
            if original != sorted(subgrid):
                valid = False
                break
    
    for column in matrix['columns']:
        if original != sorted(column):
            valid = False
            break

    if valid:
        print('SIM\n')
    else:
        print('NAO\n')