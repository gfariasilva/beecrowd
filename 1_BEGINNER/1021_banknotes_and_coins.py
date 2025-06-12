money, cents = map(int, input().strip().split('.'))

coins = {
    1.00:0,
    0.50:0,
    0.25:0,
    0.10:0,
    0.05:0,
    0.01:0
}

notes = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0
}

for coin in coins.keys():
    div = cents // (coin * 100)
    if div >= 1:
        coins[coin] += int(div)
        cents -= coin * 100 * div

for note in notes.keys():
    div = money // note
    if div >= 1:
        notes[note] += int(div)
        money -= note * div

coins[1] += money

print('NOTAS:')
for key, value in notes.items():
    print(f'{value} nota(s) de R$ {key}.00')

print('MOEDAS:')
for key, value in coins.items():
    print(f'{value} moeda(s) de R$ {"{:.2f}".format(key)}')