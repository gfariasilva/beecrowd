notes = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

money = int(input().strip())
new_money = money

for note in notes.keys():
    div = new_money // note
    if div >= 1:
        notes[note] += int(div)
        new_money -= note * div

notes[1] += new_money

print(money)
for key, value in notes.items():
    print(f'{value} nota(s) de R$ {key},00')