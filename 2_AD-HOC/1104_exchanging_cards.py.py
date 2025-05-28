while True:
    a, b = map(int, input().strip().split())

    if not a and not b:
        break

    a_cards = set(map(int, input().strip().split()))
    b_cards = set(map(int, input().strip().split()))

    equal = list(map(lambda x: x in b_cards, a_cards))

    len_a = len(a_cards) - equal.count(True)
    len_b = len(b_cards) - equal.count(True)

    print(min(len_a, len_b))